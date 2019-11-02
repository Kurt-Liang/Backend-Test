# Backend-Test

objectives1  
1. 使用sysbench壓測mysql  
    1-1. oltp測試  
    1-2. innodb  
    1-3. size=1000000  
    1-4. time=120s
2. 結果截屏至: StressTestReport.PDF  

objectives2
1. 對pcap解析  
    1-1. 用TShark先將所有資料轉成output.csv  
        1-1-1. 原本使用python-scapy解析，但是記憶體不足導致python被系統直接關閉，只好增加Swap解決  
        1-1-2. 解決後因為解析速度太慢才換成使用TShark  
    1-2. 使用python獲取output.csv裡的資料，將需要的資料用pymysql創建test表，最後把資料輸入至test表  
        1-2-1. backendtest庫(事先創建好)  
        1-2-2. test表  
             id int primary key auto_increment  
	     Date char(10)  
	     time char(10)  
	     usec char(10)  
	     SourceIP char(30)  
	     SourcePort char(10)  
	     DestinationIP char(30)  
	     DestinationPort char(10)  
	     FQDN char(60)  

2. 寫一個CLI menu程式  
    2-1. main.py為主程式  
        2-1-1. 執行main.py時會先連接至MySQL，再輸出menu.py裡的show_menu()方法  
        2-1-2. 依照輸入的指令去find.py中使用對應的方法，並輸出欲查詢的資料  
        2-1-3. 輸出的資料依照Date->time->usec按升序排序，並以50單位為一頁  
        2-1-4. 實現換頁功能還有結束時能回到show_menu()  

objectives3
1. 使用nginx架設網站伺服器  
2. 寫一個PHP檔  
    2-1. 實現PHP連接MySQL  
        2-1.1 如果MySQL為開啟狀態，則在頁面顯示json格式的{"mysql_status":"OK"}  
        2-1.2 如果MySQL為關閉狀態，則在頁面顯示json格式的{"mysql_status":"ERROR"}  
3. 寫一個config.ini設定檔  
    3-1. 實現控制monitor.py  
4. 寫一個monitor.py  
    4-1. 監測config.ini給的URL  
    4-2. 獲取頁面json格式的response  
        4-2-1. 響應成功且MySQL為開啟狀態。log:[20190708 09:32:09.284321]OK:PID:32471,response:{"mysql_status":"OK"}  
        4-2-2. 響應成功但MySQL為關閉狀態。log:[20190708 09:31:09.284321] ERROR:PID:32472,response:{"mysql_status":"ERROR"}  
        4-2-3. 響應失敗。log:[20190708 09:31:09.284321]ERROR:PID:32473,ERROR-Can’t connect to Http://127.0.0.1/healthy.php  
    4-3. 將log增加至/home/logs/test.log  
5. 使用CornTab，每五分鐘執行一次monitor.py  
    5-1. 在Corntab中加入命令: */5 * * * * python /backendtest/monitor.py  



