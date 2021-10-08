from django.urls import path
from django.conf.urls import url
from Bigflow.FA import views
urlpatterns = [
    # FA Pages
    #url(r'^(?P<template_name>[\w-]+)/$', views.FA_Template , name='FA_Template'),
    path('fa_summary/', views.fa_summary, name="fa_summary"),
    path('fa_assetadd/', views.fa_assetadd, name="fa_assetadd"),
    path('fa_assetchecker/', views.fa_assetchecker, name="fa_assetchecker"),
    path('fa_capdate_change/', views.fa_capdate_change, name="fa_capdate_change"),
    path('fa_capdate_changeplus/', views.fa_capdate_changeplus, name="fa_capdate_changeplus"),
    path('cp_datechecker/', views.fa_capdate_checker, name="fa_capdate_checker"),
    path('fa_asset_parentchild/', views.fa_asset_parentchild, name="fa_asset_parentchild"),
    path('fa_asset_parent_plus/', views.fa_asset_parent_plus, name="fa_asset_parent_plus"),
    path('fa_asset_parentchildcheck/', views.fa_asset_parentchildcheck, name="fa_asset_parentchildcheck"),
    path('fa_writeoff/', views.fa_writeoff, name="fa_writeoff"),
    path('fa_writeoffplus/', views.fa_writeoffplus, name="fa_writeoffplus"),
    path('fa_writeoff_check/', views.fa_writeoff_check, name="fa_writeoff_check"),
    path('fa_impairment/', views.fa_impairment, name="fa_impairment"),
    path('fa_impairmentplus/', views.fa_impairmentplus, name="fa_impairmentplus"),
    path('fa_impairment_check/', views.fa_impairment_check, name="fa_impairment_check"),
    path('fa_asset_merge/', views.fa_asset_merge, name="fa_asset_merge"),
    path('fa_asset_merge_plus/', views.fa_asset_merge_plus, name="fa_asset_merge_plus"),
    path('fa_asset_merge_checker/', views.fa_asset_merge_checker, name="fa_asset_merge_checker"),
    path('fa_asset_split/', views.fa_asset_split, name="fa_asset_split"),
    path('fa_asset_split_plus/', views.fa_asset_split_plus, name="fa_asset_split_plus"),
    path('fa_asset_split_checker/', views.fa_asset_split_checker, name="fa_asset_split_checker"),
    path('fa_asset_catgry/', views.fa_asset_catgry, name="fa_asset_catgry"),
    path('fa_asset_catgry_plus/', views.fa_asset_catgry_plus, name="fa_asset_catgry_plus"),
    path('fa_asset_catgrychecker/', views.fa_asset_catgrychecker, name="fa_asset_catgrychecker"),
    path('fa_asset_sale/', views.fa_asset_sale, name="fa_asset_sale"),
    path('fa_asset_saleplus/', views.fa_asset_saleplus, name="fa_asset_saleplus"),
    path('fa_asset_sale_checker/', views.fa_asset_sale_checker, name="fa_asset_sale_checker"),
    path('fa_value_reduction/', views.fa_value_reduction, name="fa_value_reduction"),
    path('fa_value_reduction_plus/', views.fa_value_reduction_plus, name="fa_value_reduction_plus"),
    path('fa_reduction_checker/', views.fa_reduction_checker, name="fa_reduction_checker"),
    path('fa_transfer_maker/', views.fa_transfer_maker, name="fa_transfer_maker"),
    path('fa_transferplus/', views.fa_transferplus, name="fa_transferplus"),
    path('fa_transfer_checker/', views.fa_transfer_checker, name="fa_transfer_checker"),
    path('fa_depreciation_calc/', views.fa_depreciation_calc, name="fa_depreciation_calc"),
    path('fa_posttocbs/', views.fa_posttocbs, name="fa_posttocbs"),
    path('fa_cwip_checker/', views.fa_cwip_checker, name="fa_cwip_checker"),
    path('fa_query_summary/',views.fa_query_summary,name="fa_query_summary"),
    path('fa_financial_year/', views.fa_financial_year, name="fa_financial_year"),
    path('fa_financial_year_plus/', views.fa_financial_year_plus, name="fa_financial_year_plus"),
    path('fa_financial_year_checker/', views.fa_financial_year_checker, name="fa_financial_year_checker"),
    path('fa_physic_verify/', views.fa_physic_verify, name="fa_physic_verify"),
    path('fa_physic_verify_plus/', views.fa_physic_verify_plus, name="fa_physic_verify_plus"),
    path('fa_physic_verify_check/', views.fa_physic_verify_check, name="fa_physic_verify_check"),

    #cat Master
    path('fa_asset_catgry_master_plus/', views.fa_asset_catgry_master_plus, name="fa_asset_catgry_master_plus"),
    path('fa_asset_catgry_summary/', views.fa_asset_catgry_summary, name="fa_asset_catgry_summary"),
    path('fa_mst_location/', views.fa_mst_location, name="fa_mst_location"),
    path('fa_image_popup/', views.fa_image_popup, name="fa_image_popup"),
    path('get_entity_branch/',views.get_entity_branch,name="get_entity_branch"),

    # FA Fuctions
    path('asset_details/', views.asset_details, name="asset_details"),
    path('drop_data/', views.drop_data, name="drop_data"),
    path('generate_saletemplate/', views.generate_saletemplate, name="generate_saletemplate"),
    path('get_branch/', views.get_branch, name="get_branch"),
    path('imageconvert_base64/', views.imageconvert_base64, name="imageconvert"),
    path('save_asset/', views.save_asset, name="save_asset"),
    path('branch_details/', views.branch_details, name="branch_details"),
    path('save_location/', views.save_location, name="save_location"),
    path('writeoff_summary/', views.writeoff_summary, name="writeoff_summary"),
    path('asset_checker/', views.asset_checker, name="asset_checker"),
    path('fa_category/', views.fa_category, name="fa_category"),
    path('fa_category_get/', views.fa_category_get, name="fa_category_get"),
    path('drop_branch/', views.drop_branch, name="drop_branch"),
    path('fa_assetadd/', views.fa_assetadd, name="fa_assetadd"),
    # path('imageconvert/', views.imageconvert, name="imageconvert"),
    path('sale_make/', views.sale_make, name="sale_make"),
    path('dep_calculation/', views.dep_calculation, name="dep_calculation"),
    path('fin_year/', views.fin_year, name="fin_year"),
    path('cust_data/', views.cust_data, name="cust_data"),
    path('dep_ratedata/', views.dep_ratedata, name="dep_ratedata"),
    path('glno_data/', views.glno_data, name="glno_data"),
    path('dep_data_get/', views.dep_data_get, name="dep_data_get"),
    path('cwip_group_get/', views.cwip_group_get, name="cwip_group_get"),
    path('data_cc/', views.data_cc, name="data_cc"),
    path('data_bs/', views.data_bs, name="data_bs"),
    path('get_state_drop/', views.get_state_drop, name="get_state_drop"),
    path('posttocbs_set/',views.posttocbs_set,name="posttocbs_set"),
    path('drop_data/', views.drop_data, name="drop_data"),
    path('save_asset/', views.save_asset, name="save_asset"),

    path('commondata_get/', views.commondata_get, name="commondata_get"),
    path('repost/', views.repost_set, name="repost"),

    #FA Clearance
    path('faclearence_unlock/', views.faclearence_unlock, name="repost"),


    #Main CSS
    path('css_main_trail/', views.css_main_trail, name="css_main_trail"),

    ## excel
    # path('dpforecast_getexcel/', views.dpforecast_getexcel, name='dpforecast_getexcel'),
    # path('dpregular_getexcel/', views.dpregular_getexcel, name='dpregular_getexcel'),
    path('check_file_exists/',views.check_file_exists,name='check_file_exists'),
    path('dpregular_getexcel/', views.fa_excel_s3, name='dpregular_getexcel'), #Directly download files
    path('dpregular_getexcel_test/', views.fa_excel, name='dpregular_getexcel_test'),
    path('dpforecast_getexcel_test/', views.dpforecast_getexcel, name='dpforecast_getexcel_test'),
    path('check_file_exists_forecast/',views.check_file_exists_forecast,name='check_file_exists_forecast'),
    path('dpforecast_getexcel/', views.fa_excel_s3_forecast, name='dpforecast_getexcel'),
]