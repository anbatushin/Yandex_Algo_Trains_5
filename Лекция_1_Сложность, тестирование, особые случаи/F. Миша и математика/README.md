<div class="problem-statement">
   <div class="header">
      <h1 class="title">F. Миша и математика</h1>
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
   <div class="legend"> Миша сидел на занятиях математики в Высшей школе экономики и решал следующую задачу: дано <!--l. 47--><math display="inline"
      style="text-indent: 0em;" xmlns="http://www.w3.org/1998/Math/MathML"><mi>n</mi></math> целых чисел и нужно расставить между
      ними знаки <!--l. 47--><math display="inline" style="text-indent: 0em;" xmlns="http://www.w3.org/1998/Math/MathML"><mo>+</mo></math>
      и <!--l. 47--><math display="inline" style="text-indent: 0em;" xmlns="http://www.w3.org/1998/Math/MathML"><mo>×</mo></math>
      так, чтобы результат полученного арифметического выражения был нечётным (например, между числами <!--l. 47--><math display="inline"
      style="text-indent: 0em;" xmlns="http://www.w3.org/1998/Math/MathML"><mn>5</mn></math>, <!--l. 47--><math display="inline"
      style="text-indent: 0em;" xmlns="http://www.w3.org/1998/Math/MathML"><mn>7</mn></math>, <!--l. 47--><math display="inline"
      style="text-indent: 0em;" xmlns="http://www.w3.org/1998/Math/MathML"><mn>2</mn></math>, можно расставить арифметические знаки
      следующим образом: <!--l. 47--><math display="inline" style="text-indent: 0em;" xmlns="http://www.w3.org/1998/Math/MathML"><mn>5</mn>
      <mo>×</mo> <mn>7</mn> <mo>+</mo> <mn>2</mn> <mo>=</mo> <mn>3</mn><mn>7</mn></math>). Так как примеры становились все больше
      и больше, а Миша срочно убегает в гости, от вас требуется написать программу решающую данную задачу. 
   </div>
   <h2>Формат ввода</h2>
   <div class="input-specification"> В первой строке содержится единственное число <!--l. 50--><math display="inline" style="text-indent: 0em;" xmlns="http://www.w3.org/1998/Math/MathML"><mi>n</mi></math>
      (<!--l. 50--><math display="inline" style="text-indent: 0em;" xmlns="http://www.w3.org/1998/Math/MathML"><mn>2</mn> <mo>≤</mo>
      <mi>n</mi> <mo>≤</mo> <mn>1</mn><msup><mrow><mn>0</mn></mrow><mrow><mn>5</mn></mrow></msup></math>). Во второй строке содержится
      <!--l. 51--><math display="inline" style="text-indent: 0em;" xmlns="http://www.w3.org/1998/Math/MathML"><mi>n</mi></math>
      целых чисел <!--l. 51--><math display="inline" style="text-indent: 0em;" xmlns="http://www.w3.org/1998/Math/MathML"><msub><mrow><mi>a</mi></mrow><mrow><mi>i</mi></mrow></msub></math>,
      разделённых пробелами (<!--l. 51--><math display="inline" style="text-indent: 0em;" xmlns="http://www.w3.org/1998/Math/MathML">
      <mo>−</mo> <mn>1</mn><msup><mrow><mn>0</mn></mrow><mrow><mn>9</mn></mrow></msup> <mo>≤</mo> <msub><mrow><mi>a</mi></mrow><mrow><mi>i</mi></mrow></msub>
      <mo>≤</mo> <mn>1</mn><msup><mrow><mn>0</mn></mrow><mrow><mn>9</mn></mrow></msup></math>). Гарантируется, что решение существует.
      
   </div>
   <h2>Формат вывода</h2>
   <div class="output-specification"> В одной строке выведите <!--l. 54--><math display="inline" style="text-indent: 0em;" xmlns="http://www.w3.org/1998/Math/MathML"><mi>n</mi>
      <mo>−</mo> <mn>1</mn></math> символ <!--l. 54--><math display="inline" style="text-indent: 0em;" xmlns="http://www.w3.org/1998/Math/MathML"><mo>+</mo></math>
      или <!--l. 54--><math display="inline" style="text-indent: 0em;" xmlns="http://www.w3.org/1998/Math/MathML"><mo>×</mo></math>,
      в результате применения которых получается нечётный результат. (Для вывода используйте соответственно знаки «+» (ASCII код—43)
      и «x» (ASCII код—120), без кавычек). 
   </div>
   <h3>Пример 1</h3>
   <table class="sample-tests">
      <thead>
         <tr>
            <th>Ввод</th>
            <th>Вывод</th>
         </tr>
      </thead>
      <tbody>
         <tr>
            <td><pre>3
5 7 2
</pre></td>
            <td><pre>x+
</pre></td>
         </tr>
      </tbody>
   </table>
   <h3>Пример 2</h3>
   <table class="sample-tests">
      <thead>
         <tr>
            <th>Ввод</th>
            <th>Вывод</th>
         </tr>
      </thead>
      <tbody>
         <tr>
            <td><pre>2
4 -5
</pre></td>
            <td><pre>+
</pre></td>