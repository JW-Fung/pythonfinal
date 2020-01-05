from flask import Flask, render_template, request
import pandas as pd
import cufflinks as cf
import plotly as py
import plotly.graph_objs as go
from pyecharts import options as opts
from pyecharts.charts import Line
from pyecharts.charts import Bar,Tab,Line,Map,Timeline,Grid,Scatter

df1 = pd.read_csv("/home/JingwenFung1111/mysite/oneenergy.csv",encoding = 'gbk')
df2 = pd.read_csv("/home/JingwenFung1111/mysite/GDP.csv",encoding = 'gbk')


app = Flask(__name__)

# 准备工作

regions_available = list(df1.Country.dropna().unique())
# cf.set_config_file(offline=True, theme="ggplot")
# py.offline.init_notebook_mode()
regions_available2 = list(df2.CountryName.dropna().unique())
# cf.set_config_file(offline=True, theme="ggplot")
# py.offline.init_notebook_mode()


@app.route('/',methods=['GET'])
def home():
    return render_template('home.html' )

@app.route('/result',methods=['GET'])
def hu_run_2019():
    data_str = df1.to_html()
    return render_template('results2.html',
                           the_res = data_str,
                           the_select_region=regions_available)

@app.route('/hurun',methods=['POST'])
def hu_run_select()-> 'html':
    the_region = request.form["the_region_selected"]
    print(the_region) # 检查用户输入
    dfs = df1.query("Country=='{}'".format(the_region))
#     df_summary = dfs.groupby("行业").agg({"企业名称":"count","估值（亿人民币）":"sum","成立年份":"mean"}).sort_values(by = "企业名称",ascending = False )
#     print(df_summary.head(5)) # 在后台检查描述性统计
#     ## user select
    # print(dfs)
#     # 交互式可视化画图
    fig = dfs.iplot(kind="bar", x="Country", asFigure=True)
    py.offline.plot(fig, filename="example1.html",auto_open=False)
    with open("example1.html", encoding="utf8", mode="r") as f:
        plot_all = "".join(f.readlines())

#     # plotly.offline.plot(data, filename='file.html')
	
#     with open("render.html", encoding="utf8", mode="r") as f:
#         plot_all = "".join(f.readlines())
			
    data_str = dfs.to_html()
    return render_template('results2.html',
                            the_plot_all = plot_all,
							# the_plot_all = [],
                            the_res = data_str,
                            the_select_region=regions_available,
                           )


regions_available1 = list(df2.CountryName.dropna().unique())


# cf.set_config_file(offline=True, theme="ggplot")
# py.offline.init_notebook_mode()


@app.route('/data', methods=['GET'])
def hu_run_():
    data_str = df2.to_html()
    return render_template('results3.html',
                           the_res=data_str,
                           the_select_region1=regions_available1)


@app.route('/hurun1', methods=['POST'])
def hu_run_select1() -> 'html':
    the_region = request.form["the_region_selected1"]
    print(the_region)  # 检查用户输入
    dfs = df2.query("CountryName=='{}'".format(the_region))
    #     df_summary = dfs.groupby("行业").agg({"企业名称":"count","估值（亿人民币）":"sum","成立年份":"mean"}).sort_values(by = "企业名称",ascending = False )
    #     print(df_summary.head(5)) # 在后台检查描述性统计
    #     ## user select
    # print(dfs)
    #     # 交互式可视化画图
    fig = dfs.iplot(kind="bar", x="CountryName", asFigure=True)
    py.offline.plot(fig, filename="example.html", auto_open=False)
    with open("example.html", encoding="utf8", mode="r") as f:
        plot_all = "".join(f.readlines())

    #     # plotly.offline.plot(data, filename='file.html')

    #     with open("render.html", encoding="utf8", mode="r") as f:
    #         plot_all = "".join(f.readlines())

    data_str1 = dfs.to_html()
    return render_template('results3.html',
                           the_plot_all=plot_all,
                           # the_plot_all = [],
                           the_res=data_str1,
                           the_select_region=regions_available1,
                           )

@app.route('/map',methods=['GET'])
def timeline_map() -> Timeline:
        return render_template('render.html')

@app.route('/12',methods=['GET'])
def country() -> Line:
        return render_template('12energy-gdp.html')

@app.route('/intro',methods=['GET'])
def introduce() -> Line:
        return render_template('introduction.html')




if __name__ == '__main__':
    app.run(debug=True,port=8000)
