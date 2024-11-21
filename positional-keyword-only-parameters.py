def tag(name,*content,class_=None,**attrs):
    """Generate one or more HTML tags"""
    if class_ is not None:
        attrs['class'] = class_
    attrs_pairs = (f' {attr}="{value}"' for attr,value in sorted(attrs.items()))
    attrs_str = ''.join(attrs_pairs)
    if content:
        elements=(f'<{name}{attrs_str}>{c}</{name}>' for c in content)
        return '\n'.join(elements)
    else:
        return f'<{name}{attrs_str} />'

# keyword-only parameter    
def f(a,*,b):
    return a, b

# Positional-only parameters
def divmod(a,b,/):
    return (a // b, a % b)
    

if __name__=='__main__':
    # Testando as varias formas como a função tag pode ser usada graças a positional e Keyword-only parametros
    print(tag('br'))
    print(tag('p','hello'))
    print(tag('p','hello','world'))
    print(tag('p','hello',id=33))
    print(tag('p','hello','world',class_='sidebar'))
    print(tag(content='testing',name='img'))
    my_tag = {
        'name':'img',
        'title':'Sunset Boulevard',
        'src':'sunset.jpg',
        'class':'framed'
    }
    print(tag(**my_tag))

    # b só pode ser passado como keyword-only parameter
    print(f(1,b=2))

    try:
        print(f(1,2))
    except TypeError as e:
        print(e)

    # Positional-only parameters
    print(divmod(10,2))
    try:
        print(divmod(a=10,b=2))
    except TypeError as e:
        print(e)