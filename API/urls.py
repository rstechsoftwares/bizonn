from django.urls import path
from API.views.ProductViews import *
from API.views.RetailerViews import *
from API.views.WholesellerViews import *
from API.views.ManufacturerViews import *



app_name = 'API'

urlpatterns = [

    # ======== Product Enpoints =======
    path("get-all-products", GetAllProductView, name="GetAllProducts"),
    path("get-products-by-id", GetProductByIDView, name="GetProductsByID"),
    path("create-products", CreateProductView, name="CreateProducts"),
    path("update-products", UpdateProductView, name="UpdateProducts"),
    path("delete-products", DeleteProductView, name="DeleteProducts"),

    # ======== Retailer Endpoints =======
    path("get-all-retailers", GetAllRetailerView, name="GetAllRetailers"),
    path("get-retailers-by-id", GetRetailerByIDView, name="GetRetailerByID"),
    path("create-retailer", CreateRetailerView, name="CreateRetailer"),
    path("update-retailer", UpdateRetailerView, name="UpdateRetailer"),
    path("delete-retailer", DeleteRetailerView, name="DeleteRetailer"),

    # ======== Wholeseller Endpoints =======
    path("get-all-wholesellers", GetAllWholesellerView, name="GetAllWholesellers"),
    path("get-wholeseller-by-id", GetWholesellerByIDView, name="GetWholesellerByID"),
    path("create-wholeseller", CreateWholesellerView, name="CreateWholeseller"),
    path("update-wholeseller", UpdateWholesellerView, name="UpdateWholeseller"),
    path("delete-wholeseller", DeleteWholesellerView, name="DeleteWholeseller"),

    # ======== Manufacturer Endpoints =======
    path("get-all-manufactures", GetAllManufacturerView, name="GetAllManufactures"),
    path("get-manufacture-by-id", GetManufacturerByIDView, name="GetManufactureByID"),
    path("create-manufacture", CreateManufacturerView, name="CreateManufacture"),
    path("update-manufacture", UpdateManufacturerView, name="UpdateManufacture"),
    path("delete-manufacture", DeleteManufacturerView, name="DeleteManufacture"),


]