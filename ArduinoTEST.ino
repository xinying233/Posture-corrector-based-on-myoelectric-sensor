void setup() {

  Serial.begin(9600);
}


void loop() {
  int sensorValue = analogRead(A0);
  float voltage = sensorValue * (5.0 / 1023.0);//从外部肌电模块读取的数值（0-5V量程）
  int v=100+(voltage*100);//除去小数点，防止数据传输时传出小数点
  Serial.print(170,HEX);//检查字符串10101010（0xAA），保证每次数值输出的第一个值为有效值
  Serial.print(v);//实时传出数据
  delay(100);//踩点画图
 
}
