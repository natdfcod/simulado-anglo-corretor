with open('dados.txt','r') as arquivo:
    res=input('digita suas resposta: ')
    x=y=z=y1=y2=y3=y4=y5=y6=y7=y8=y9=y10=0
    for linha in arquivo:
        q=int(linha.split('.')[0])
        gaba=linha.split('.')[1]
        # print(f'{gaba} e {res}')
        if gaba==res[x]:
            print(q,'correto')
            y=y+1
        else:
            print(f'{q} errado')
            z=z+1
        if q<15:
             0
        #port
        elif q==15:
            p=y*4/15
        #hist
        elif q<=27:
            if gaba==res[x]:
                    y1=y1+1
        #geo
        elif q<=39:
             if gaba==res[x]:
                    y2=y2+1
        #bio
        elif q<=51:
             if gaba==res[x]:
                    y3=y3+1
        #fis
        elif q<=63:
             if gaba==res[x]:
                    y4=y4+1
        #qui
        elif q<=75:
             if gaba==res[x]:
                    y5=y5+1
        #mat
        elif q<=90:
             if gaba==res[x]:
                    y6=y6+1
        #ingl
        elif q<=95:
             if gaba==res[x]:
                    y7=y7+1
        #espan
        elif q<=100:
            2
        #arte
        elif q<=105:
             if gaba==res[x]:
                    y8=y8+1
        #filo
        elif q<=110:
             if gaba==res[x]:
                    y9=y9+1
        #socio
        elif q<=115:
             if gaba==res[x]:
                    y10=y10+1
        x=x+1
    n=float(2*y/23)
    o = float("{:.2f}".format(n))
    h=y1*4/12
    g=y2*4/12
    b=y3*4/12
    f=y4*4/12
    q=y5*4/12
    m=y6*4/15
    i=y7*4/5
    a=y8*4/5
    fi=y9*4/5
    s=y10*4/5
    print(f'vc acertou {y} e errou {z}')
    print(f'vc tirou {o} de 10')
    print(f'{"%.2f" % p} em português')
    print(f'{"%.2f" % h} em historia')
    print(f'{"%.2f" % g} em geografia')
    print(f'{"%.2f" % b} em biologia')
    print(f'{"%.2f" % f} em fisica')
    print(f'{"%.2f" % q} em quimica')
    print(f'{"%.2f" % m} em matematica')
    print(f'{"%.2f" % i} em ingles')
    print(f'{"%.2f" % a} em artes')
    print(f'{"%.2f" % fi} em filosofia')
    print(f'{"%.2f" % s} em sociologia')
   














