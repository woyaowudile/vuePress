from selenium import webdriver
import time

driver = webdriver.Chrome()

# # driver.get('https://www.baidu.com/')
# # time.sleep(1)
# # # label = driver.find_element_by_class_name('s-bottom-layer-content')
# # # label = driver.find_element_by_id('bottom_layer')
# # # label = driver.find_element_by_tag_name('p')
# # label = driver.page_source
# # # label = driver.find_element_by_partial_link_text('京公网')
# # print(label)

# # driver.close()

# driver.get('https://xiaoke.kaikeba.com/example/X-Man/')
# time.sleep(5)

# teacher = driver.find_element_by_class_name('form-teacher')
# teacher.send_keys('小K老师')

# assistant = driver.find_element_by_class_name('form-assist')
# assistant.send_keys('都喜欢')

# time.sleep(2)

# button = driver.find_element_by_id('submit')
# button.click()

# time.sleep(5)
# driver.close()


# 课中练习， 获取音乐的所有评论

driver.get('https://y.qq.com/n/yqq/song/001qvvgF38HVc4.html') # 访问页面
time.sleep(2)

clickformore = driver.find_element_by_class_name('js_get_more_hot')
time.sleep(0.5)

clickformore.click()
comments = driver.find_element_by_class_name('js_hot_list').find_elements_by_class_name('js_cmt_li') # 使用class_name找到评论

print(len(comments))

for i in range(len(comments)): # 循环
    comment = comments[i].find_element_by_tag_name('p') # 找到评论
    print ('评论'+str(i)+':'+comment.text + '\n-------------------------------------------------') # 打印评论

driver.close() # 关闭浏览器