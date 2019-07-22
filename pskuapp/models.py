# This is an auto-generated Django model module.
# You'll have to do the following manually to clean this up:
#   * Rearrange models' order
#   * Make sure each model has one field with primary_key=True
#   * Make sure each ForeignKey has `on_delete` set to the desired behavior.
#   * Remove `managed = False` lines if you wish to allow Django to create, modify, and delete the table
# Feel free to rename the models, but don't rename db_table values or field names.
from __future__ import unicode_literals

from django.db import models


class AmaPskuMapping(models.Model):
    time_perd_type_code = models.CharField(db_column='TIME_PERD_TYPE_CODE', max_length=20)
    time_perd_end_date = models.CharField(db_column='TIME_PERD_END_DATE', max_length=20)
    mkt_name = models.CharField(db_column='MKT_NAME', max_length=50)
    mkt_lvl_name = models.CharField(db_column='MKT_LVL_NAME', max_length=20)
    mkt_cntry_name = models.CharField(db_column='MKT_CNTRY_NAME', max_length=50)
    prod_name = models.CharField(db_column='PROD_NAME', max_length=200)
    prod_lvl_name = models.CharField(db_column='PROD_LVL_NAME', max_length=20)
    level1 = models.CharField(db_column='LEVEL1', max_length=50, blank=True, null=True)
    level2 = models.CharField(db_column='LEVEL2', max_length=50, blank=True, null=True)
    level3 = models.CharField(db_column='LEVEL3', max_length=50, blank=True, null=True)
    level4 = models.CharField(db_column='LEVEL4', max_length=50, blank=True, null=True)
    level5 = models.CharField(db_column='LEVEL5', max_length=50, blank=True, null=True)
    level6 = models.CharField(db_column='LEVEL6', max_length=50, blank=True, null=True)
    level7 = models.CharField(db_column='LEVEL7', max_length=50, blank=True, null=True)
    level8 = models.CharField(db_column='LEVEL8', max_length=50, blank=True, null=True)
    company = models.CharField(db_column='COMPANY', max_length=50, blank=True, null=True)
    brand = models.CharField(db_column='BRAND', max_length=50, blank=True, null=True)
    sales_mu_qty = models.DecimalField(db_column='SALES_MU_QTY', max_digits=21, decimal_places=5, blank=True,
                                       null=True)
    sales_mu_qty_ya = models.DecimalField(db_column='SALES_MU_QTY_YA', max_digits=21, decimal_places=5, blank=True,
                                          null=True)
    sales_msu_qty = models.DecimalField(db_column='SALES_MSU_QTY', max_digits=21, decimal_places=5, blank=True,
                                        null=True)
    sales_msu_qty_ya = models.DecimalField(db_column='SALES_MSU_QTY_YA', max_digits=21, decimal_places=5, blank=True,
                                           null=True)
    sales_mlc_amt = models.DecimalField(db_column='SALES_MLC_AMT', max_digits=21, decimal_places=5, blank=True,
                                        null=True)
    sales_mlc_amt_ya = models.DecimalField(db_column='SALES_MLC_AMT_YA', max_digits=21, decimal_places=5, blank=True,
                                           null=True)
    sales_musd_amt = models.DecimalField(db_column='SALES_MUSD_AMT', max_digits=21, decimal_places=5, blank=True,
                                         null=True)
    sales_musd_amt_ya = models.DecimalField(db_column='SALES_MUSD_AMT_YA', max_digits=21, decimal_places=5,
                                            blank=True,
                                            null=True)
    numrc_dist_pct = models.DecimalField(db_column='NUMRC_DIST_PCT', max_digits=21, decimal_places=5, blank=True,
                                         null=True)
    numrc_dist_pct_ya = models.DecimalField(db_column='NUMRC_DIST_PCT_YA', max_digits=21, decimal_places=5,
                                            blank=True,
                                            null=True)
    wgt_dist_pct = models.DecimalField(db_column='WGT_DIST_PCT', max_digits=21, decimal_places=5, blank=True,
                                       null=True)
    wgt_dist_pct_ya = models.DecimalField(db_column='WGT_DIST_PCT_YA', max_digits=21, decimal_places=5, blank=True,
                                          null=True)
    power_flag = models.CharField(db_column='POWER_FLAG', max_length=10, blank=True,
                                  null=True)
    psku_nd_threshold = models.DecimalField(db_column='PSKU_ND_THRESHOLD', max_digits=21, decimal_places=5,
                                            blank=True,
                                            null=True)
    nd_dya_psku = models.DecimalField(db_column='ND_DYA_PSKU', max_digits=21, decimal_places=5, blank=True,
                                      null=True)
    wd_dya_psku = models.DecimalField(db_column='WD_DYA_PSKU', max_digits=21, decimal_places=5, blank=True,
                                      null=True)
    nd_threshold_del_psku = models.DecimalField(db_column='ND_THRESHOLD_DEL_PSKU', max_digits=21, decimal_places=5,
                                                blank=True, null=True)
    growing_threshold_chk_psku = models.DecimalField(db_column='GROWING_THRESHOLD_CHK_PSKU', max_digits=21,
                                                     decimal_places=5, blank=True,
                                                     null=True)
    declining_threshold_chk_psku = models.DecimalField(db_column='DECLINING_THRESHOLD_CHK_PSKU', max_digits=21,
                                                       decimal_places=5, blank=True,
                                                       null=True)
    power = models.CharField(db_column='POWER', max_length=20, blank=True, null=True)
    power_sku = models.CharField(db_column='POWER_SKU', max_length=20, blank=True,
                                 null=True)
    declining_threshold_pwr_chk = models.DecimalField(db_column='DECLINING_THRESHOLD_PWR_CHK', max_digits=21,
                                                      decimal_places=5, blank=True,
                                                      null=True)
    growing_threshold_pwr_chk = models.DecimalField(db_column='GROWING_THRESHOLD_PWR_CHK', max_digits=21,
                                                    decimal_places=5, blank=True,
                                                    null=True)
    key_psku = models.CharField(db_column='KEY_PSKU', max_length=300, blank=True,
                                null=True)
    key_psku_mth = models.CharField(db_column='KEY_PSKU_MTH', max_length=300, blank=True,
                                    null=True)
    short_category_name = models.CharField(db_column='SHORT_CATEGORY_NAME', max_length=50, blank=True,
                                           null=True)
    cbu = models.CharField(db_column='CBU', max_length=50, blank=True, null=True)
    market_type = models.CharField(db_column='MARKET_TYPE', max_length=50, blank=True,
                                   null=True)
    region = models.CharField(db_column='REGION', max_length=50, blank=True, null=True)
    ama_total = models.CharField(db_column='AMA_TOTAL', max_length=20, blank=True,
                                 null=True)
    key_chnl_brnd_mth = models.CharField(db_column='KEY_CHNL_BRND_MTH', max_length=300, blank=True,
                                         null=True)
    cc_code = models.CharField(db_column='CC_CODE', max_length=10)
    last_load_date = models.DateTimeField(db_column='LAST_LOAD_DATE', blank=True,
                                          null=True)
    key_item_mth_psku = models.CharField(db_column='KEY_ITEM_MTH_PSKU', max_length=300, blank=True,
                                         null=True)
    wd_target = models.DecimalField(db_column='WD_TARGET', max_digits=21, decimal_places=5, blank=True,
                                    null=True)
    psku_id = models.AutoField(db_column='PSKU_ID', primary_key=True)

    class Meta:
        managed = False
        db_table = 'AMA_PSKU_MAPPING'

# class AmaPskuMapping(models.Model):
#     time_perd_type_code = models.CharField(db_column='TIME_PERD_TYPE_CODE', max_length=50)
#     time_perd_end_date = models.CharField(db_column='TIME_PERD_END_DATE', max_length=50)
#     mkt_name = models.CharField(db_column='MKT_NAME', max_length=50)
#     mkt_lvl_name = models.CharField(db_column='MKT_LVL_NAME', max_length=50)
#     mkt_cntry_name = models.CharField(db_column='MKT_CNTRY_NAME', max_length=50)
#     prod_name = models.CharField(db_column='PROD_NAME', max_length=100)
#     prod_lvl_name = models.CharField(db_column='PROD_LVL_NAME', max_length=50)
#     level1 = models.CharField(db_column='LEVEL1', max_length=50)
#     level2 = models.CharField(db_column='LEVEL2', max_length=50)
#     level3 = models.CharField(db_column='LEVEL3', max_length=50)
#     level4 = models.CharField(db_column='LEVEL4', max_length=50)
#     level5 = models.CharField(db_column='LEVEL5', max_length=50)
#     level6 = models.CharField(db_column='LEVEL6', max_length=50)
#     level7 = models.CharField(db_column='LEVEL7', max_length=50)
#     level8 = models.CharField(db_column='LEVEL8', max_length=50)
#     company = models.CharField(db_column='COMPANY', max_length=50)
#     brand = models.CharField(db_column='BRAND', max_length=50)
#     sales_mu_qty = models.FloatField(db_column='SALES_MU_QTY')
#     sales_mu_qty_ya = models.FloatField(db_column='SALES_MU_QTY_YA', blank=True, null=True)
#     sales_msu_qty = models.FloatField(db_column='SALES_MSU_QTY')
#     sales_msu_qty_ya = models.FloatField(db_column='SALES_MSU_QTY_YA', blank=True, null=True)
#     sales_mlc_amt = models.FloatField(db_column='SALES_MLC_AMT')
#     sales_mlc_amt_ya = models.FloatField(db_column='SALES_MLC_AMT_YA', blank=True, null=True)
#     sales_musd_amt = models.FloatField(db_column='SALES_MUSD_AMT')
#     sales_musd_amt_ya = models.FloatField(db_column='SALES_MUSD_AMT_YA', blank=True, null=True)
#     numrc_dist_pct = models.FloatField(db_column='NUMRC_DIST_PCT')
#     numrc_dist_pct_ya = models.FloatField(db_column='NUMRC_DIST_PCT_YA', blank=True, null=True)
#     wgt_dist_pct = models.FloatField(db_column='WGT_DIST_PCT')
#     wgt_dist_pct_ya = models.FloatField(db_column='WGT_DIST_PCT_YA', blank=True, null=True)
#     power_flag = models.CharField(db_column='POWER_FLAG', max_length=50)
#     psku_nd_threshold = models.FloatField(db_column='PSKU_ND_THRESHOLD', blank=True, null=True)
#     nd_dya_psku = models.FloatField(db_column='ND_DYA_PSKU', blank=True, null=True)
#     wd_dya_psku = models.FloatField(db_column='WD_DYA_PSKU', blank=True, null=True)
#     nd_threshold_del_psku = models.FloatField(db_column='ND_THRESHOLD_DEL_PSKU', blank=True, null=True)
#     growing_threshold_chk_psku = models.FloatField(db_column='GROWING_THRESHOLD_CHK_PSKU')
#     declining_threshold_chk_psku = models.FloatField(db_column='DECLINING_THRESHOLD_CHK_PSKU')
#     power = models.BooleanField(db_column='POWER')
#     power_sku = models.BooleanField(db_column='POWER_SKU')
#     declining_threshold_pwr_chk = models.FloatField(db_column='DECLINING_THRESHOLD_PWR_CHK')
#     growing_threshold_pwr_chk = models.FloatField(db_column='GROWING_THRESHOLD_PWR_CHK')
#     key_psku = models.CharField(db_column='KEY_PSKU', max_length=100)
#     key_psku_mth = models.CharField(db_column='KEY_PSKU_MTH', max_length=150)
#     short_category_name = models.CharField(db_column='SHORT_CATEGORY_NAME', max_length=50)
#     cbu = models.CharField(db_column='CBU', max_length=50)
#     market_type = models.CharField(db_column='MARKET_TYPE', max_length=50)
#     region = models.CharField(db_column='REGION', max_length=50)
#     ama_total = models.CharField(db_column='AMA_TOTAL', max_length=50)
#     key_chnl_brnd_mth = models.CharField(db_column='KEY_CHNL_BRND_MTH', max_length=100)
#     cc_code = models.CharField(db_column='CC_CODE', max_length=50)
#     last_load_date = models.DateTimeField(db_column='LAST_LOAD_DATE')
#     key_item_mth_psku = models.CharField(db_column='KEY_ITEM_MTH_PSKU', max_length=50)
#     wd_target = models.CharField(db_column='WD_TARGET', max_length=50)
#     psku_id = models.IntegerField(db_column='PSKU_ID', primary_key=True)
#
#     class Meta:
#         managed = False
#         db_table = 'AMA_PSKU_MAPPING'
