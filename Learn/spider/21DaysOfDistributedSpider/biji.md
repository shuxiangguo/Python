### 下载文件的 Files Pipeline: 
####当使用Files Pipeline下载文件的时候，按照以下步骤完成：
1. 定义好一个Item，然后在这个Item里面定义俩个属性，分别为file_urls以及files。file_urls是用来存储
需要下载的文件的url链接，是一个列表。
2. 当文件下载完成后，会把文件下载的相关信息存储到item的files属性中，比如下载路径、下载的url和文件的校验码等
3. 在配置文件settings.py中配置FILES_STORE，这个配置是用来设置文件下载下来的路径。
4. 启动pipeline：在ITEM_PIPELINES中设置scrapy.pipelines.files.FilesPipeline:1

###下载图片的 Images Pipeline
####当使用Images Pipeline下载文件的时候，按照以下步骤完成：
1. 定义好一个Item，然后在这个Item里面定义俩个属性，分别为image_urls以及images。images_urls是用来存储
需要下载的文件的url链接，是一个列表。
2. 当文件下载完成后，会把文件下载的相关信息存储到item的images属性中，比如下载路径、下载的url和文件的校验码等
3. 在配置文件settings.py中配置IMAGES_STORE，这个配置是用来设置文件下载下来的路径。
4. 启动pipeline：在ITEM_PIPELINES中设置scrapy.pipelines.images.ImagesPipeline:1