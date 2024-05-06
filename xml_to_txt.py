from bs4 import BeautifulSoup as bs

path_r = 'C:/Users/ASUS/Desktop/helmet detection/annotations/hard_hat_workers'
path_w = 'D:/helmet_text_files/hard_hat_workers'

for j in range(5000):
    
    path = path_r + str(j) + '.xml'

    with open(path, 'r') as f:
        raw_data = f.read()
        
    data = bs(raw_data, "xml")
    
    img_size = data.find('size')
    
    img_width = int(img_size.find('width').text)
    img_height = int(img_size.find('height').text)
    img_depth = int(img_size.find('depth').text)
    
    object_lst = data.find_all('object')
    
    line_lst = list()
    
    for obj in object_lst:
        
        label = obj.find('name').text
        
        if label == 'helmet':
            label_code = '0'
        elif label == 'head':
            label_code = '1'
        else:
            label_code = '2'
            
        x1 = int(obj.find('xmin').text)
        y1 = int(obj.find('ymin').text)
        x2 = int(obj.find('xmax').text)
        y2 = int(obj.find('ymax').text)
        
        #print('label:', label)
        #print('x1:', x1)
        #print('y1:', y1)
        #print('x2:', x2)
        #print('y2:', y2)
        #print(type(x1))
        
        x = float((x1 + x2)/(2*img_width))
        y = float((y1 + y2)/(2*img_height))
        w = float((x2 - x1)/img_width)
        h = float((y2 - y1)/img_height)
        
        line_str = label_code + ' ' + str(x) + ' ' + str(y) + ' ' + str(w) + ' ' + str(h)
        line_lst.append(line_str)

    path_dest = path_w + str(j) + '.txt'

    with open(path_dest, 'w') as f:
        for line in line_lst:
            f.write(line)
            f.write('\n')
    f.close()
    
    
    
    
    
    
    
    
    
    
    






