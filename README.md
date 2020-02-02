# waosper
这些代码仅在Ubuntu端测试过

download_jason_unruhe.py 	批量频道视频下载 	4 minutes ago

main.py 	对批量频道视频/字幕下载和电子书整理功能的更新 	1 minute ago

rcm.py 	这些天写的代码 	12 days ago

recode.py 	对批量频道视频/字幕下载和电子书整理功能的更新 	1 minute ago

rund.py 	对批量频道视频/字幕下载和电子书整理功能的更新 	1 minute ago

subd.py 	对批量频道视频/字幕下载和电子书整理功能的更新 	1 minute ago

trout.py 	对批量频道视频/字幕下载和电子书整理功能的更新 	1 minute ago

un7z.py 	对批量频道视频/字幕下载和电子书整理功能的更新 	1 minute ago

unpdf.py 	对批量频道视频/字幕下载和电子书整理功能的更新 	1 minute ago

unuvz_copy.py 	这些天写的代码 	12 days ago

unzip.py

download_jason_unruhe.py是『半自动』下载视频和生成视频组（videoGroup.txt）文件的代码，需要手动新建文件：missing.txt、pass_setting.txt和 视频介绍.txt

依赖：rcm.py，这是网络爬虫，爬取视频组的代码

main.py是『全自动』解压电子书压缩包的代码，依赖：un7z.py

recode.py是『全自动』除去文件名乱码的代码

rund.py是一个辅助调用Ubuntu系统命令的代码

subd.py是『半自动』依赖于视频组文件下载字幕的代码

trout.py是调用Ubuntu系统命令（tree）生成电子书文件树的代码

un7z.py是调用Ubuntu下的解压软件（7z）来解压某一路径下所有的（不包括子目录）压缩包的代码，依赖于rund.py

unpdf.py是调用PDF文件中PDF的标题信息来修正文件名的代码，是recode.py的辅助

unuvz_copy.py是un7z.py的最原始版本

unzip.py是rund.py的原型

不保证rund.py可以正常发挥作用，之前误删过一次，这次是重写的（根据unzip.py）
