import datetime
import os
from subprocess import Popen,PIPE

def get_extension(filepath):
    splits = filepath.split(".")
    if len(splits) == 1:
       ext = ''
    else:
       ext = splits[len(splits) - 1]
    return ext

def get_basename(filepath):
    base_name = os.path.basename(filepath)
    return os.path.splitext(base_name)[0]

def create_raster_proxy(s3path=None):

    stime = datetime.datetime.utcnow()


    cache_dir = r'Z:\mrf'
    proxy_dir = r'C:\Users\greg6750\Documents\IPython Notebooks\developing-with-imagery\Week 1'
    proxy_ext = 'mrf'

    ds_name = os.path.basename(s3path)
    ds_noext = get_basename(ds_name)
    ds_ext = get_extension(s3path)

    #proto = 'vsis3'
    proto = 'vsicurl' #landsat
    #proto = 'vsiaz'

    s3_key = '/{0}/{1}'.format(proto,s3path).replace('\n','').replace('\r','')
    if not os.path.isdir(proxy_dir):
        os.mkdir(proxy_dir)


    data_name = '{0}/{1}.mrf_cache'.format(cache_dir,ds_noext)
    proxy_path = '{0}/{1}.{2}'.format(proxy_dir,ds_noext,proxy_ext)

    print(s3_key)


    gdal_translate_location = r"C:\PROJECTS\OptimizeRasters\GDAL\bin\gdal_translate.exe"
    gdal_translate = [gdal_translate_location,'-of', 'MRF', '-co', 'NOCOPY=TRUE', '-co','BLOCKSIZE=512','-co','UNIFORM_SCALE=2','-co','COMPRESS=LERC','-co', 'OPTIONS="V2=ON"']#, '-co', 'AWS_S3_ENDPOINT=https://s3.us-west-2.amazonaws.com', '-co','AWS_VIRTUAL_HOSTING=no']
    gdal_translate.extend([s3_key, proxy_path, '-co', 'CACHEDSOURCE={0}'.format(s3_key), '-co', 'DATANAME={0}'.format(data_name),'-co', 'INDEXNAME={0}'.format(data_name)])
    gdal_process = Popen(gdal_translate, shell=True, stdout=PIPE, stderr=PIPE)
    stdout, stderr = gdal_process.communicate()
    if stderr:
        print("GDAL stderr:","DEBUG")
        print(stderr,"DEBUG")


    return proxy_dir


s3_path = "http://naipblobs.blob.core.windows.net/naip/data/v1/2011/states/al/al_1m_2011/30085/m_3008501_ne_16_1_20110815.mrf"
#s3_path = 'http://landsatarchives.s3.amazonaws.com/C1/ETM/004/025/1999/LE07_L1GT_004025_19990816_20170217_01_T2/LE07_L1GT_004025_19990816_20170217_01_T2_B1.tif'

create_raster_proxy(s3_path)
