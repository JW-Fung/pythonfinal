## 一、项目主题
一次能源的能源强度水平和各国环境的关系
## 二、负责部分
HTML页面及CSS样式，连接页面，编写页面内容，用python连接数据与html文档，搭建调试flask项目，部署Pythonanywhere
## 三、项目目的
能源强度表面使用多少能源来生产一个单位的经济产出，较低的比率表示使用较少的能量来产生一个单位的输出。本次报告想研究一次能源的使用率高低对环境的影响，包括森林面积、二氧化碳排放等；还加入了经济指标，如GDP。
## [Pythonanywhere项目部署入口](http://jingwenfung1111.pythonanywhere.com/)
## 四、总结说明
### 1.总述：本项目共有8个URL,4个交互图，两个数据筛选图     
图表页面  [地图](http://jingwenfung1111.pythonanywhere.com/map)   [各国一次能源使用率](http://jingwenfung1111.pythonanywhere.com/result)   [各国GDP](http://jingwenfung1111.pythonanywhere.com/data)   [十二国一次能源与GDP关系](http://jingwenfung1111.pythonanywhere.com/12)    
 基本交互功能的HTML5控件丰富
### 2.github文档格式
文档格式正确，包含基本的templates、static、app.py/main.py、数据文档csv
### 3.技术文档书写
* HTML档描述    
①home页面框架用jQuery的插件，用bootstrap的插件，导航和轮播图，使网页更加完善，美观。    
②运用了RWD响应式网页设计，使网站根据用户的设备环境进行相应的响应和调整，使用户体验更好。      
③运用栅格系统，使网站更加工整简洁，美观。     
④运用了内嵌和外链CSS，使网页更加美观。       
⑤运用悬浮，实现用户与网站的交互，   
* Python档描述    
①利用flask创建项目，用路由规则与url构建，使项目拥有多个页面   
②运用多个模块，flask、pandas、cufflinks、plotly、pyecharts，使项目更加丰富    
③运用函数传递信息与数据，利用return返回页面，使项目主程序更加简洁    
④实现筛选数据，使项目实现交互    

* Web App动作描述     
①网站的导航、数据表、轮播图、各按钮都可以实现页面跳转。   
②图表页面按钮实现数据筛选并跳转页面。    
③数据表和轮播图实现与用户悬浮交互。    
     
  
 
