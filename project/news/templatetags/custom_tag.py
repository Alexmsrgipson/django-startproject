# @register.simple_tags(takes_context=True)
# def url_replace(context, **kwargs):
#    d = context['request'].GET.copy()
#    for k, v in kwargs.items():
#        d[k] = v
#    return d.urlencode()