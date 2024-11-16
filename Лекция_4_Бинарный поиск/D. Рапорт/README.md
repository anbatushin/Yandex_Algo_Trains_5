<div class="problem-statement">
   <div class="header">
      <h1 class="title">D. Рапорт</h1>
      <table>
         <tr class="time-limit">
            <td class="property-title">Ограничение времени</td>
            <td>2&nbsp;секунды</td>
         </tr>
         <tr class="memory-limit">
            <td class="property-title">Ограничение памяти</td>
            <td>256Mb</td>
         </tr>
         <tr class="input-file">
            <td class="property-title">Ввод</td>
            <td colspan="1">стандартный ввод или input.txt</td>
         </tr>
         <tr class="output-file">
            <td class="property-title">Вывод</td>
            <td colspan="1">стандартный вывод или output.txt</td>
         </tr>
      </table>
   </div>
   <h2></h2>
   <div class="legend"> Верс нужно подготовить рапорт о последнем боевом вылете. Она уже сочинила в голове текст, осталось лишь его записать. Рапорт
      будет состоять из двух частей: первая будет содержать <!--l. 47--><math display="inline" style="text-indent: 0em;" xmlns="http://www.w3.org/1998/Math/MathML"><mi>n</mi></math>
      слов, <!--l. 47--><math display="inline" style="text-indent: 0em;" xmlns="http://www.w3.org/1998/Math/MathML"><mi>i</mi></math>-е
      из которых состоит из <!--l. 47--><math display="inline" style="text-indent: 0em;" xmlns="http://www.w3.org/1998/Math/MathML"><msub><mrow><mi>a</mi></mrow><mrow><mi>i</mi></mrow></msub></math>
      букв, вторая — <!--l. 47--><math display="inline" style="text-indent: 0em;" xmlns="http://www.w3.org/1998/Math/MathML"><mi>m</mi></math>
      слов, <!--l. 47--><math display="inline" style="text-indent: 0em;" xmlns="http://www.w3.org/1998/Math/MathML"><mi>j</mi></math>-е
      из которых состоит из <!--l. 47--><math display="inline" style="text-indent: 0em;" xmlns="http://www.w3.org/1998/Math/MathML"><msub><mrow><mi>b</mi></mrow><mrow><mi>j</mi></mrow></msub></math>
      букв. Язык Крии не содержит никаких знаков препинания. Верс должна записать рапорт на клетчатом рулоне бумаги, шириной <!--l.
      47--><math display="inline" style="text-indent: 0em;" xmlns="http://www.w3.org/1998/Math/MathML"><mi>w</mi></math> клеток.
      Так как рапорт состоит из двух частей, она разделит вертикальной чертой рулон на две части целой ширины, после чего в левой
      части напишет первую часть, а в правой — вторую. <!--l. 49-->
      <p style="text-indent: 0em;">Обе части рапорта записываются аналогично, каждая на своей части рулона. Одна буква слова занимает
      ровно одну клетку. Первое слово записывается в первой строке рулона, начиная с самой левой клетки этой части рулона. Каждое
      следующее слово, если это возможно, должно быть записано в той же строке, что и предыдущее, и быть отделено от него ровно
      одной пустой клеткой. Иначе, оно пишется в следующей строке, начиная с самой левой клетки. Если ширина части рулона меньше,
      чем длина какого-то слова, которое должно быть написано в этой части, написать эту часть рапорта на части рулона такой ширины
      невозможно. <!--l. 51-->
      </p><p style="text-indent: 0em;">Гарантируется, что можно провести вертикальную черту так, что обе части рапорта возможно
      написать. Верс хочет провести вертикальную черту так, чтобы длина рулона, которой хватит, чтобы написать рапорт, была минимальна.
      Помогите ей найти эту минимальную длину. </p>
      <p></p>
      
   </div>
   <h2>Формат ввода</h2>
   <div class="input-specification"> В первой строке даны три целых числа <!--l. 55--><math display="inline" style="text-indent: 0em;" xmlns="http://www.w3.org/1998/Math/MathML"><mi>w</mi></math>,
      <!--l. 55--><math display="inline" style="text-indent: 0em;" xmlns="http://www.w3.org/1998/Math/MathML"><mi>n</mi></math>
      и <!--l. 55--><math display="inline" style="text-indent: 0em;" xmlns="http://www.w3.org/1998/Math/MathML"><mi>m</mi></math>
      — ширина рулона, количество слов в первой и второй части рапорта (<!--l. 55--><math display="inline" style="text-indent: 0em;"
      xmlns="http://www.w3.org/1998/Math/MathML"><mn>1</mn> <mo>≤</mo> <mi>w</mi> <mo>≤</mo> <mn>1</mn><msup><mrow><mn>0</mn></mrow><mrow><mn>9</mn></mrow></msup></math>;
      <!--l. 55--><math display="inline" style="text-indent: 0em;" xmlns="http://www.w3.org/1998/Math/MathML"><mn>1</mn> <mo>≤</mo>
      <mi>n</mi><mo>,</mo><mi>m</mi> <mo>≤</mo> <mn>1</mn><mn>0</mn><mn>0</mn><mspace width="0.3em"><mn>0</mn><mn>0</mn><mn>0</mn></mspace></math>).
      <!--l. 57-->
      <p style="text-indent: 0em;">В следующей строке дано <!--l. 57--><math display="inline" style="text-indent: 0em;" xmlns="http://www.w3.org/1998/Math/MathML"><mi>n</mi></math>
      целых чисел <!--l. 57--><math display="inline" style="text-indent: 0em;" xmlns="http://www.w3.org/1998/Math/MathML"><msub><mrow><mi>a</mi></mrow><mrow><mi>i</mi></mrow></msub></math>
      — длина <!--l. 57--><math display="inline" style="text-indent: 0em;" xmlns="http://www.w3.org/1998/Math/MathML"><mi>i</mi></math>-го
      слова первой части рапорта <!--l. 57--><math display="inline" style="text-indent: 0em;" xmlns="http://www.w3.org/1998/Math/MathML"><mn>1</mn>
      <mo>≤</mo> <msub><mrow><mi>a</mi></mrow><mrow><mi>i</mi></mrow></msub> <mo>≤</mo> <mn>1</mn><msup><mrow><mn>0</mn></mrow><mrow><mn>9</mn></mrow></msup></math>.
      <!--l. 59-->
      </p><p style="text-indent: 0em;">В следующей строке дано <!--l. 59--><math display="inline" style="text-indent: 0em;" xmlns="http://www.w3.org/1998/Math/MathML"><mi>m</mi></math>
      целых чисел <!--l. 59--><math display="inline" style="text-indent: 0em;" xmlns="http://www.w3.org/1998/Math/MathML"><msub><mrow><mi>b</mi></mrow><mrow><mi>j</mi></mrow></msub></math>
      — длина <!--l. 59--><math display="inline" style="text-indent: 0em;" xmlns="http://www.w3.org/1998/Math/MathML"><mi>j</mi></math>-го
      слова второй части рапорта <!--l. 59--><math display="inline" style="text-indent: 0em;" xmlns="http://www.w3.org/1998/Math/MathML"><mn>1</mn>
      <mo>≤</mo> <msub><mrow><mi>b</mi></mrow><mrow><mi>j</mi></mrow></msub> <mo>≤</mo> <mn>1</mn><msup><mrow><mn>0</mn></mrow><mrow><mn>9</mn></mrow></msup></math>.
      <!--l. 61-->
      </p><p style="text-indent: 0em;">Гарантируется, что возможно провести черту так, что обе части рапорта возможно написать.
      </p>
      <p></p>
      <p></p>
      
   </div>
   <h2>Формат вывода</h2>
   <div class="output-specification"> В единственной строке выведите одно целое число — минимальную длину рулона, которой достаточно, чтобы написать рапорт. </div>
   <h2>Пример</h2>
   <table class="sample-tests">
      <thead>
         <tr>
            <th>Ввод</th>
            <th>Вывод</th>
         </tr>
      </thead>
      <tbody>
         <tr>
            <td><pre>15 6 6
2 2 2 3 2 2
3 3 5 2 4 3
</pre></td>
            <td><pre>3
</pre></td>
         </tr>
      </tbody>
   </table>
   <h2>Примечания</h2>
   <div class="notes"> В тесте из примера рулон можно разделить на две части, проведя черту между 7 и 8 столбцом клеток, а затем записать по два
      слова в каждой строке в обеих частях рапорта. 
   </div>