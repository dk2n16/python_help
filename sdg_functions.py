"""Python functions to run analysis of SDG indicators"""
from pathlib import Path
import geopandas as gpd
import pandas as pd

def very_very_simple_function():  # Note that nothing is being passed into this function
    print("Hello")

def very_simple_function(name):  # Note that something is being passed into this function (i.e. name)
    print('Hello ' + name)


def very_simple_addition_function(x, y):
    """Prints the sum of x + y (EVERTHING IS BEING DONE IN THE FUNCTION - NOTHING IS BEING RETURNED)"""
    print(x + y)

def very_simple_multiplication_function(x, y):
    """RETURNS the product of x * y (A VARIABLE IS BEING RETURNED HERE TO WHERE THE FUNCTION IS CALLED"""
    z = x * y
    return z  # This means that z is being sent back from the function

def very_simple_option_argument_function(name, time_of_day="Morning"):
    print("Good " + time_of_day + " " + name)

def open_geodataframe(shapefile_path, cols=None, index=None):
    """
    Returns gdf of shapefile. If cols is None, all cols will be returned, else only cols in a list. If index is None, no index will be set

    Parameters:
    -----------
    shapefile_path (str):
        Path to shapefile

    cols (None/list):
        Columns to select. If left as default (None), all columns will be selected (Default=None)

    index (None/str):
        Column to set as index - If left as default (None), no index will be set (Default = None)

    Returns:
    --------
    gdf (gpd.GeoDataFrame):
        Geodataframe of shapefile opened with columns and index set as selected

    """
    shp = Path(str(shapefile_path)).resolve()
    gdf = gpd.read_file(shp)
    if cols:
        gdf = gdf[cols]
    if index:
        gdf = gdf.set_index(index)
    return gdf



if __name__ == "__main__":
    print("very_very_simple_function()")
    very_very_simple_function()
    name = 'John'
    print("very_simple_function(name)")
    very_simple_function(name)  # this should print 'John'
    print("very_simple_addition_function(2, 3)")
    very_simple_addition_function(2, 3) #this should print 5
    x = 2
    y = 6
    print("very_simple_multiplication_function(x, y)")
    z = very_simple_multiplication_function(x, y) # Note that a variable is assigned here so that something can be returned to it
    print("very_simple_option_argument_function(name)")
    very_simple_option_argument_function(name) #For this one the default value for time_of_day will be used
    very_simple_option_argument_function(name, time_of_day="Afternoon")  # For this one Afternoon will be used
    very_simple_option_argument_function(name, time_of_day="Evening")  # For this one Evening will be used



    # SHAPEFILE_PATH = r'D:\SDGS\15_1_1\data\boundaries\Local_Authority_Districts__December_2019__Boundaries_UK_BFE.shp'
    # cols = ['LAD19CD', 'LAD19NM', 'LAD19NMW', 'BNG_E', 'BNG_N', 'geometry']
    # index = 'LAD19CD'
    # gdf_1 = open_geodataframe(SHAPEFILE_PATH) #This one will open the default way with all columns and no index set
    # print(gdf_1.head())
    # #-------------------------------------------
    # #OPEN ONLY CERTAIN COLS
    # #-------------------------------------------
    # gdf_2 = open_geodataframe(SHAPEFILE_PATH, cols=cols)
    # print(gdf_2.head())
    # print(gdf_2.columns)
    #
    # #-------------------------------------------
    # #SET INDEX
    # #-------------------------------------------
    # gdf_3 = open_geodataframe(SHAPEFILE_PATH, index=index)
    # print(gdf_3.head())
    #
    # # -------------------------------------------
    # # SET INDEX AND SELECT COLS
    # # -------------------------------------------
    # gdf_4 = open_geodataframe(SHAPEFILE_PATH, cols=cols, index=index)
    # print(gdf_4.head())




