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

def open_geodataframe(shapefile_path, cols=None, index=None, epsg=27700):
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

    epsg (int):
        EPSG Code for gdf coordinate reference system

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
    if not gdf.crs.to_epsg() == epsg:  # Set the projection to that defined in epsg in the arguments
        gdf = gdf.to_crs(epsg)
    return gdf

def do_spatial_join(gdf_LA, gdf_forest):
    """
    Returns spatial join of LAs with forests

    Parameters:
    -----------
    gdf_LA (gpd.GeoDataFrame):
        Geodataframe of Local Authorities

    gdf_forest (gpd.GeoDataFrame):
        Geodataframe of forests

    Returns:
    --------
    gdf_join (gpd.GeoDataFrame):
        GeodataFrame of forests joined to LAS
-
    """
    print("WRITE CODE TO DO JOIN AND RETURN JOINED GDF")
    # CODE
    # return gdf_join

def calculate_area(gdf_join):
    """
    Returns geodataframe of area of forest per LA

    Parameters:
    -----------
    gdf_join (gpd.GeoDataFrame):
        Geodataframe of forests joined to LAs

    Returns:
    --------
    gdf_area (gpd.GeoDataFrame):
        GeoDataFrame with area calculated
    """
    print('WRITE CODE TO CALCULATE AREAS')
    # CODE
    # return gdf_area



if __name__ == "__main__":
# ###########################################################################################
                    ### THIS IS THE BEGINNING
# ###########################################################################################
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
# ###########################################################################################
                    ### THIS IS THE BEGINNING - ENDED
# ###########################################################################################



# ###########################################################################################
                    ### THIS IS THE FUNCTIONS TO READ GEODATAFRAMES
# ###########################################################################################
# ----------------------------------------------------------------------------------------------------------------------
#     BASE_DIRECTORY = Path(__file__).resolve().parent.joinpath('data')
#     LA = BASE_DIRECTORY.joinpath('boundaries/LA_NI.shp')  # Path to LA Shapefile
#     cols = ['LAD19CD', 'LAD19NM', 'LAD19NMW', 'BNG_E', 'BNG_N', 'geometry']
#     index = 'LAD19CD'
#     gdf_1 = open_geodataframe(LA) # This one will open the default way with all columns and no index set
#     print(gdf_1.head())
#     # -------------------------------------------
#     # OPEN ONLY CERTAIN COLS
#     # -------------------------------------------
#     gdf_2 = open_geodataframe(LA, cols=cols)
#     print(gdf_2.head())
#     print(gdf_2.columns)
#
#     # -------------------------------------------
#     #SET INDEX
#     # -------------------------------------------
#     gdf_3 = open_geodataframe(LA, index=index)
#     print(gdf_3.head())
#
#     # -------------------------------------------
#     # SET INDEX AND SELECT COLS
#     # -------------------------------------------
#     gdf_4 = open_geodataframe(LA, cols=cols, index=index)
#     print(gdf_4.head())

# ###########################################################################################
                    ### THIS IS THE FUNCTIONS TO READ GEODATAFRAMES - ENDED
# ###########################################################################################



# ###########################################################################################
                    ### THIS IS THE PART YOU NEED TO WRITE
# ###########################################################################################
# ----------------------------------------------------------------------------------------------------------------------

    # # -------------------------------------------
    # # Loop through a list of paths and open the shapefiles
    # # -------------------------------------------
    # BASE_DIRECTORY = Path(__file__).resolve().parent.joinpath('data')  # This points to the folder holding the forests
    # FORESTS = [x for x in BASE_DIRECTORY.joinpath('forests').iterdir() if x.name.endswith('.shp')]  # Making a list of shapefiles (end in .shp) in the BASE_DIRECTORY
    # print(FORESTS)
    # LA = BASE_DIRECTORY.joinpath('boundaries/LA_NI.shp')  # Path to LA Shapefile
    # cols = ['LAD19CD', 'LAD19NM', 'LAD19NMW', 'BNG_E', 'BNG_N', 'geometry']
    # index = 'LAD19CD'
    # gdf_LA = open_geodataframe(LA)
    # print(gdf_LA.head())
    # SAM_GDF = pd.read_csv(BASE_DIRECTORY.joinpath('SAM/SAM_LAD_DEC_2019_UK.csv'))
    # print(SAM_GDF.head())
    # for forest in FORESTS:
    #     gdf_forest = open_geodataframe(forest)
    #     print(gdf_forest.head())
    #     gdf_join = do_spatial_join(gdf_LA, gdf_forest)
    #     gdf_area = calculate_area(gdf_join)
    #     #gdf_final = calculate_proportion_forest(gdf_area, SAM_GDF)






