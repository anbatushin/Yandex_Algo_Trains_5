<div class="problem-statement">
   <div class="header">
      <h1 class="title">C. Форматирование файла</h1>
      <table>
         <tr class="time-limit">
            <td class="property-title">Ограничение времени</td>
            <td>1&nbsp;секунда</td>
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
   <div class="legend"> Петя - начинающий программист. Сегодня он написал код из <!--l. 47--><math display="inline" style="text-indent: 0em;" xmlns="http://www.w3.org/1998/Math/MathML"><mi>n</mi></math>
      строк. <!--l. 49-->
      <p style="text-indent: 0em;">К сожалению оказалось, что этот код трудно читать. Петя решил исправить это, добавив в различные
      места пробелы. А точнее, для <!--l. 49--><math display="inline" style="text-indent: 0em;" xmlns="http://www.w3.org/1998/Math/MathML"><mi>i</mi></math>-й
      строки ему нужно добавить <span style="font-weight: bold;">ровно </span><!--l. 49--><math display="inline" style="text-indent:
      0em;" xmlns="http://www.w3.org/1998/Math/MathML"><msub><mrow><mi>a</mi></mrow><mrow><mi>i</mi></mrow></msub></math> пробелов.
      <!--l. 51-->
      </p><p style="text-indent: 0em;">Для добавления пробелов Петя выделяет строку и нажимает на одну из трёх клавиш: <span style="font-family:
      monospace;">Space</span>, <span style="font-family: monospace;">Tab</span>, и <span style="font-family: monospace;">Backspace</span>.
      При нажатии на <span style="font-family: monospace;">Space </span>в строку добавляется один пробел. При нажатии на <span style="font-family:
      monospace;">Tab </span>в строку добавляются четыре пробела. При нажатии на <span style="font-family: monospace;">Backspace
      </span>в строке удаляется один пробел. <!--l. 53-->
      </p><p style="text-indent: 0em;">Ему хочется узнать, какое наименьшее количество клавиш придётся нажать, чтобы добавить необходимое
      количество пробелов в каждую строку. Помогите ему! </p>
      <p></p>
      <p></p>
      
   </div>
   <h2>Формат ввода</h2>
   <div class="input-specification"> Первая строка входных данных содержит одно целое положительное число <!--l. 56--><math display="inline" style="text-indent:
      0em;" xmlns="http://www.w3.org/1998/Math/MathML"><mi>n</mi></math><!--l. 56--><math display="inline" style="text-indent: 0em;"
      xmlns="http://www.w3.org/1998/Math/MathML"><mrow><mo>(</mo><mrow><mn>1</mn> <mo>≤</mo> <mi>n</mi> <mo>≤</mo> <mn>1</mn><msup><mrow><mn>0</mn></mrow><mrow><mn>5</mn></mrow></msup></mrow><mo>)</mo></mrow></math>
      – количество строк в файле. <!--l. 58-->
      <p style="text-indent: 0em;">Каждая из следующих <!--l. 58--><math display="inline" style="text-indent: 0em;" xmlns="http://www.w3.org/1998/Math/MathML"><mi>n</mi></math>
      строк содержит одно целое неотрицательное число <!--l. 58--><math display="inline" style="text-indent: 0em;" xmlns="http://www.w3.org/1998/Math/MathML"><msub><mrow><mi>a</mi></mrow><mrow><mi>i</mi></mrow></msub></math><!--l.
      58--><math display="inline" style="text-indent: 0em;" xmlns="http://www.w3.org/1998/Math/MathML"><mrow><mo>(</mo><mrow><mn>0</mn>
      <mo>≤</mo> <msub><mrow><mi>a</mi></mrow><mrow><mi>i</mi></mrow></msub> <mo>≤</mo> <mn>1</mn><msup><mrow><mn>0</mn></mrow><mrow><mn>9</mn></mrow></msup></mrow><mo>)</mo></mrow></math>
      – количество пробелов, которые нужно добавить в <!--l. 58--><math display="inline" style="text-indent: 0em;" xmlns="http://www.w3.org/1998/Math/MathML"><mi>i</mi></math>-ю
      строку файла. </p>
      
   </div>
   <h2>Формат вывода</h2>
   <div class="output-specification"> Выведите одно число – минимальное количество нажатий, чтобы добавить в каждой строке необходимое количество пробелов. </div>
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
            <td><pre>5
1
4
12
9
0
</pre></td>
            <td><pre>8
</pre></td>
         </tr>
      </tbody>
   </table>
   <h2>Примечания</h2>
   <div class="notes"> В примере можно: <ul>
      <li>1 раз нажать на <span style="font-family: monospace;">Space </span>в первой строке. </li>
      <li>1 раз нажать на <span style="font-family: monospace;">Tab </span>на второй строке. </li>
      <li>3 раза нажать на <span style="font-family: monospace;">Tab </span>в третьей строке. </li>
      <li>2 раза нажать на <span style="font-family: monospace;">Tab </span>и один раз нажать на <span style="font-family: monospace;">Space
      </span>в четвёртой строке. </li>
      <li>Ничего не нажимать в пятой строке.</li>
      </ul>
      <!--l. 74-->
      <p style="text-indent: 0em;">В итоге получается <!--l. 74--><math display="inline" style="text-indent: 0em;" xmlns="http://www.w3.org/1998/Math/MathML"><mn>1</mn>
      <mo>+</mo> <mn>1</mn> <mo>+</mo> <mn>3</mn> <mo>+</mo> <mn>3</mn> <mo>=</mo> <mn>8</mn></math> нажатий. Можно доказать, что
      нельзя добавить необходимое количество пробелов за <!--l. 74--><math display="inline" style="text-indent: 0em;" xmlns="http://www.w3.org/1998/Math/MathML"><mn>7</mn></math>
      нажатий или меньше. </p>
      
   </div>