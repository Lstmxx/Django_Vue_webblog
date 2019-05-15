from django.shortcuts import render

# Create your views here.
from .models import User,Paper,Kind
from .models import To_DB
from django.shortcuts import HttpResponse
from django.core.serializers import serialize
import json
from django.views.decorators.csrf import csrf_exempt
import hashlib
from .uitls import markdown_to_html
@csrf_exempt
def add(request):
    Paperlist = []
    k = Kind.objects.get(num = '1')
    u = User.objects.get(uid = 1)
    for x in range(21,30):
        Paperlist.append(Paper(name='Vue搞起来'+str(x),
                                kinds=k,
                                author=u,
                                ))
    Paper.objects.bulk_create(Paperlist)
    #User.objects.create(name = 'lsm')
    #whereDict = {"name": "lsm", }
    # print(request.method)
    # if request.method == 'POST':
    #     print(request.body)
    #     data = json.loads(request.body,strict=False)
    #     print(data)
    #     wheredict = data
    #     selectdict = ""
    #     res = ""
    #     res = To_DB(obj=User,op="insert",wheredict=wheredict,selectdict=selectdict)
    #     res = list(To_DB(obj=User,op="query",wheredict={},selectdict={'*':''}))
    #     print(res)
    #     res = json.dumps(res)
    res = '失败'

    return HttpResponse(res)

@csrf_exempt
def test(request):
    data = []
    datad = {}
    res = ''
    res = markdown_to_html.md_to_html()
    print(type(res))
    datad['html'] = res
    data.append(datad)
    data = json.dumps(data)
    return HttpResponse(data)

@csrf_exempt
def login_or_register(request):
    md5 = hashlib.md5()
    res = ''
    rsp = []
    rsp_d = {}
    if request.method == 'POST':
        data = json.loads(request.body,strict=False)
        res = User.objects.filter(name=data['usn']).values_list()
        res_len = len(res)
        md5.update(data['pwd'].encode("utf8"))
        al_pwd = md5.hexdigest()
        if res_len == 0:
            if data['status']==1:
                rsp_d['resluts'] = "还没注册兄dei"
                rsp_d['status'] = '0'
                rsp.append(rsp_d)
            if data['status'] == 0:
                rsp_d['resluts'] = "注册成功"
                rsp_d['status'] = '1'
                rsp.append(rsp_d)
                whereDict = {
                "name":data['usn'],
                "pwd":al_pwd
                }
                res = To_DB(obj = User,op = "insert",wheredict = whereDict,selectdict={})
                print(res)
        else:
            pwd = res[0][1]
            if data['status']==1:
                if pwd == al_pwd:
                    rsp_d['resluts'] = "登录成功"
                    rsp_d['status'] = '2'
                    rsp.append(rsp_d)
                else:
                    rsp_d['resluts'] = "账号已存在"
                    rsp_d['status'] = '3'
                    rsp.append(rsp_d)
        print(rsp)
        rsp = json.dumps(rsp)
        return HttpResponse(rsp)

@csrf_exempt
def query(request):
    name_dict = {}
    res = ''
    if request.method  == "POST":
        data = json.loads(request.body,strict=False)
        kind_name = data['type'][1:]
        k_id = Kind.objects.filter(name = kind_name).values_list('num')
        res = Paper.objects.filter(kinds = k_id[0][0]).values('name','author','publish_time')
        for num,i in enumerate(res):
            if name_dict.__contains__(i['author'])==False:
                n = User.objects.filter(uid=i['author']).values('name')
                name_dict[i['author']] = n[0]['name']
            res[num]['author']=name_dict[i['author']]
            res[num]['publish_time']=res[num]['publish_time'].strftime("%Y-%m-%d %H:%M:%S")
        res = json.dumps(list(res))
    return HttpResponse(res)

@csrf_exempt
def get_paper_by_id(request):
    res = ''
    if request.method == 'POST':
        data = json.loads(request.body,strict=False)
        ID = data['id'] 
        res = Paper.objects.filter(id=ID).values()
        res = list(res)
        n = User.objects.filter(uid=res[0]['author_id']).values('name')
        res[0]['author_id'] = n[0]['name']
        res[0]['publish_time'] = res[0]['publish_time'].strftime("%Y-%m-%d %H:%M:%S")
        res[0]['modify_time'] = res[0]['modify_time'].strftime("%Y-%m-%d %H:%M:%S")
        res = json.dumps(res)
    return HttpResponse(res)