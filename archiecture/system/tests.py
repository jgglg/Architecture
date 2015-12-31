# --*-- coding: utf-8 --*--
from archiecture.deco import require_permission

'''
require_permission装饰器的参数是你创建的permission的codename
'''


@require_permission("menu_custmer")
def test_case(request):
    print "goooooooood"