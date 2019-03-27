from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
from django.template.defaultfilters import length

poll_list = [
        {
		'id': 1,
		'title': 'การสอนวิชา Web Programming',
		'questions': [
			{
				'text': 'อาจารย์บัณฑิตสอนน่าเบื่อไหม',
				'choices': [
					{'text': 'น่าเบื่อมาก', 'value': 1},
					{'text': 'ค่อนข้างน่าเบื่อ', 'value': 2},
					{'text': 'เฉยๆ', 'value': 3},
					{'text': 'ค่อนข้างสนุก', 'value': 4},
					{'text': 'สนุกมากๆ', 'value': 5}
				]
			},
			{
				'text': 'นักศึกษาเรียนรู้เรื่องหรือไม่',
				'choices': [
					{'text': 'ไม่รู้เรื่องเลย', 'value': 1},
					{'text': 'รู้เรื่องนิดหน่อย', 'value': 2},
					{'text': 'เฉยๆ', 'value': 3},
					{'text': 'เรียนรู้เรื่อง', 'value': 4},
					{'text': 'เรียนเข้าใจมากๆ', 'value': 5}
				]
			},
			{
				'text': 'เครื่องคอมพิวเตอร์ใช้งานดีหรือไม่',
				'choices': [
					{'text': 'เครื่องช้ามาก', 'value': 1},
					{'text': 'เครื่องค่อนข้างช้า', 'value': 2},
					{'text': 'เฉยๆ', 'value': 3},
					{'text': 'เครื่องเร็ว', 'value': 4},
					{'text': 'เครื่องเร็วมากๆ', 'value': 5}
				]
			},

		]
	},
        {
		'id': 2,
		'title': 'ความยากข้อสอบ mid-term',
		'questions': [
			{
				'text': 'ข้อ 1',
				'choices': [
					{'text': 'ง่ายมากๆ', 'value': 1},
					{'text': 'ค่อนข้างง่าย', 'value': 2},
					{'text': 'เฉยๆ', 'value': 3},
					{'text': 'ค่อนข้างยาก', 'value': 4},
					{'text': 'ยากมากๆ', 'value': 5}
				]
			},
			{
				'text': 'ข้อ 2',
				'choices': [
					{'text': 'ง่ายมากๆ', 'value': 1},
					{'text': 'ค่อนข้างง่าย', 'value': 2},
					{'text': 'เฉยๆ', 'value': 3},
					{'text': 'ค่อนข้างยาก', 'value': 4},
					{'text': 'ยากมากๆ', 'value': 5}
				]
			},
			{
				'text': 'ข้อ 3',
				'choices': [
					{'text': 'ง่ายมากๆ', 'value': 1},
					{'text': 'ค่อนข้างง่าย', 'value': 2},
					{'text': 'เฉยๆ', 'value': 3},
					{'text': 'ค่อนข้างยาก', 'value': 4},
					{'text': 'ยากมากๆ', 'value': 5}
				]
			},
			{
				'text': 'ข้อ 4',
				'choices': [
					{'text': 'ง่ายมากๆ', 'value': 1},
					{'text': 'ค่อนข้างง่าย', 'value': 2},
					{'text': 'เฉยๆ', 'value': 3},
					{'text': 'ค่อนข้างยาก', 'value': 4},
					{'text': 'ยากมากๆ', 'value': 5}
				]
			},
			{
				'text': 'ข้อ 5',
				'choices': [
					{'text': 'ง่ายมากๆ', 'value': 1},
					{'text': 'ค่อนข้างง่าย', 'value': 2},
					{'text': 'เฉยๆ', 'value': 3},
					{'text': 'ค่อนข้างยาก', 'value': 4},
					{'text': 'ยากมากๆ', 'value': 5}
				]
			},
			{
				'text': 'ข้อ 6',
				'choices': [
					{'text': 'ง่ายมากๆ', 'value': 1},
					{'text': 'ค่อนข้างง่าย', 'value': 2},
					{'text': 'เฉยๆ', 'value': 3},
					{'text': 'ค่อนข้างยาก', 'value': 4},
					{'text': 'ยากมากๆ', 'value': 5}
				]
			},

		]
	},

        {
		'id': 4,
		'title': 'อาหารที่ชอบ',
		'questions': [
			{
				'text': 'พิซซ่า',
				'choices': [
					{'text': 'ไม่ชอบเลย', 'value': 1},
					{'text': 'ค่อนข้างไม่ชอบ', 'value': 2},
					{'text': 'เฉยๆ', 'value': 3},
					{'text': 'ค่อนข้างชอบ', 'value': 4},
					{'text': 'ชอบมากๆ', 'value': 5}
				]
			},
			{
				'text': 'ไก่ทอด',
				'choices': [
					{'text': 'ไม่ชอบเลย', 'value': 1},
					{'text': 'ค่อนข้างไม่ชอบ', 'value': 2},
					{'text': 'เฉยๆ', 'value': 3},
					{'text': 'ค่อนข้างชอบ', 'value': 4},
					{'text': 'ชอบมากๆ', 'value': 5}
				]
			},
			{
				'text': 'แฮมเบอร์เกอร์',
				'choices': [
					{'text': 'ไม่ชอบเลย', 'value': 1},
					{'text': 'ค่อนข้างไม่ชอบ', 'value': 2},
					{'text': 'เฉยๆ', 'value': 3},
					{'text': 'ค่อนข้างชอบ', 'value': 4},
					{'text': 'ชอบมากๆ', 'value': 5}
				]
			},

		]
	},
    ]
def index(request):
    # poll_list = [
    #     {'id': 1, 'title': '123'},
    #     {'id': 2, 'title': '234'},
    #     {'id': 3, 'title': '345'},
    # ]
    context = {
        'page_title': 'welcome to ,y poll',
        'poll_list': poll_list
    }
    return render(request,'polls/index.html',context=context)

def detail(request,id1):
    for i in range(len(poll_list)):
        j = poll_list[i]["id"]
        if(id1 == str(j)):
            context = {
                'poll_list': poll_list[i]
            }
            break
        # else:
        #     context = {
        #         'poll_list': poll_list[i]
        #      }
    return render(request,'polls/detail.html',context=context)

# def detail(request,id):
#     return HttpResponse("detail %s"% (str(id)))