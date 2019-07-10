from django.http import HttpResponse
from django.template import Template,Context

def personal(request):
    string="""
    <html>
        <head>
            <title> 
             personal   
            </title>
            <style> 
                *{
                    padding: 0;
                    margin: 0;
                    box-sizing: border-box;
                }           
                .a{
                    background-color: skyblue;
                    
                    width: 300px;
                    height: 296px;
                    float: left;
                    
                }
                .b{                    
                    color:red;
                    font-size:30px;
                    margin-right: -3px;
                    padding:12px;
                    width: 300px;
                    height: 296px; 
                    float: left;                               
                }
                .c{
                    width: 630px;
                    height: 300px;
                    background-color: #ccffff;
                    border:2px black dotted;                                    
                }                
                
            </style>    
        </head>
        <body>
        
        {% for line in student %}
            <div class="c">
            
                <div class="a">
                    <p style="dispaly:block;">
                        <img src="{{line.picture}}" style="width:300px;height:296px;">
                    </p>
                </div>
                <div class="b">                    
                    <p style="background-color: #0033FF;">
                        姓名：{{line.name}}
                    </p>
                    <p style="background-color: #0066FF;">
                        年龄：{{line.age}}
                    </p>                    
                    <p style="background-color: #00ccFF;">
                        爱好 :
                        {% for hobby in line.hobby.items %}
                            <p style="background-color: #00FFFF;">
                                {{ hobby }}
                            </p>
                        {% endfor %}
                    </p> 
                </div>
                     
            </div>         
        {% endfor %}                        
        </boy>
    </html>
    """
    dicts={
        "student":[
        {"name": "张三", "age": 19,"picture": "https://timgsa.baidu.com/timg?image&quality=80&size=b9999_10000&sec=1562662354052&di=c7ffa6e776bfc190ecf61be1fffd4cfc&imgtype=0&src=http%3A%2F%2Fcrawler-fs.intsig.net%2Fcamfs%2Fdownload%3Ffilename%3D10005_8513f2acdb83490e4956ff9f1f51f76f_2.jpeg",
         "hobby": {"吃饭" : "10%", "睡觉" : "10%","play" : "10%", "python" : "10%"}},
        {"name": "李四", "age": 23,"picture": "https://ss3.bdstatic.com/70cFv8Sh_Q1YnxGkpoWK1HF6hhy/it/u=2231006068,3335104017&fm=26&gp=0.jpg",
         "hobby": {"吃饭" : "10%", "睡觉" : "10%","play" : "10%",  "python" : "10%"}},
        {"name": "王五", "age": 13,"picture": "https://ss1.bdstatic.com/70cFvXSh_Q1YnxGkpoWK1HF6hhy/it/u=3375533062,1775565001&fm=26&gp=0.jpg",
         "hobby": {"吃饭" : "10%", "睡觉" : "10%","play" : "10%",  "python" : "10%"}},
        {"name": "张大", "age": 21,"picture": "https://timgsa.baidu.com/timg?image&quality=80&size=b9999_10000&sec=1562662736165&di=47652216eb1bd93f904daada0871f85d&imgtype=0&src=http%3A%2F%2Fgss0.baidu.com%2F-vo3dSag_xI4khGko9WTAnF6hhy%2Fzhidao%2Fpic%2Fitem%2F4a36acaf2edda3cce9c36ccd03e93901213f923c.jpg",
         "hobby": {"吃饭" : "10%", "睡觉" : "10%","play" : "10%",  "python" : "10%"}},
        {"name": "张大", "age": 21,"picture": "https://ss0.bdstatic.com/70cFvHSh_Q1YnxGkpoWK1HF6hhy/it/u=430668890,2169277792&fm=27&gp=0.jpg",
         "hobby": {"吃饭" : "10%", "睡觉" : "10%", "play" : "10%", "python" : "10%"}}

        ]
    }

    t=Template(string)
    c=Context(dicts)
    result=t.render(c)
    return HttpResponse(result)