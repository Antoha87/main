# -*- coding: utf-8 -*-
from django.core.management.base import BaseCommand
from slugify import slugify
import xlrd
from django.core.exceptions import ObjectDoesNotExist, MultipleObjectsReturned
from catalog.models import FileProcessing, Goods, GoodsVariation


class Command(BaseCommand):

    def handle(self, *args, **options):
        fileprocessing = FileProcessing.objects.first()
        if fileprocessing:

            rb = xlrd.open_workbook(fileprocessing.fileprocessing.path, formatting_info=True)
            sheet = rb.sheet_by_index(0)
            for rownum in range(sheet.nrows):

                if not rownum == 0:
                    row = sheet.row_values(rownum)
                    print(row[1])
                    if row[1] != '' or row[2] != '':
                        if row[2] != '':
                            try:
                                p = Goods.objects.get(article=row[2])
                                p.in_stock = row[14]
                                p.save()
                                try:
                                    r = GoodsVariation.objects.get(goods=p, price_product=row[10])
                                except MultipleObjectsReturned:
                                    GoodsVariation.objects.filter(goods=p).delete()
                                    r = GoodsVariation()
                                    r.goods = p
                                    r.price_product = row[10]
                                    r.save()
                            except ObjectDoesNotExist:
                                pass
