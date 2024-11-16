<div class="problem-statement">
   <div class="header">
      <h1 class="title">B. Одномерный морской бой</h1>
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
   <div class="legend"> Поле в игре в одномерный морской бой имеет размеры <!--l. 47--><math display="inline" style="text-indent: 0em;" xmlns="http://www.w3.org/1998/Math/MathML"><mn>1</mn>
      <mo>×</mo> <mi>n</mi></math>. Ваша задача&nbsp;— найти такое максимальное <!--l. 47--><math display="inline" style="text-indent:
      0em;" xmlns="http://www.w3.org/1998/Math/MathML"><mi>k</mi></math>, что на поле можно расставить один корабль размера <!--l.
      47--><math display="inline" style="text-indent: 0em;" xmlns="http://www.w3.org/1998/Math/MathML"><mn>1</mn> <mo>×</mo> <mi>k</mi></math>,
      два корабля размера <!--l. 47--><math display="inline" style="text-indent: 0em;" xmlns="http://www.w3.org/1998/Math/MathML"><mn>1</mn>
      <mo>×</mo> <mrow><mo>(</mo><mrow><mi>k</mi> <mo>−</mo> <mn>1</mn></mrow><mo>)</mo></mrow></math>, <!--l. 47--><math display="inline"
      style="text-indent: 0em;" xmlns="http://www.w3.org/1998/Math/MathML"><mo>…</mo></math>, <!--l. 47--><math display="inline"
      style="text-indent: 0em;" xmlns="http://www.w3.org/1998/Math/MathML"><mi>k</mi></math> кораблей размера <!--l. 47--><math
      display="inline" style="text-indent: 0em;" xmlns="http://www.w3.org/1998/Math/MathML"><mn>1</mn> <mo>×</mo> <mn>1</mn></math>,
      причем корабли, как и в обычном морском бое, не должны касаться друг друга и пересекаться. 
   </div>
   <h2>Формат ввода</h2>
   <div class="input-specification"> В единственной строке входных данных дано число <!--l. 50--><math display="inline" style="text-indent: 0em;" xmlns="http://www.w3.org/1998/Math/MathML"><mi>n</mi></math>&nbsp;—
      количество клеток поля (<!--l. 50--><math display="inline" style="text-indent: 0em;" xmlns="http://www.w3.org/1998/Math/MathML"><mn>0</mn>
      <mo>≤</mo> <mi>n</mi> <mo>≤</mo> <mn>1</mn><msup><mrow><mn>0</mn></mrow><mrow><mn>1</mn><mn>8</mn></mrow></msup></math>).
      
   </div>
   <h2>Формат вывода</h2>
   <div class="output-specification"> Выведите единственное число&nbsp;— такое максимальное <!--l. 53--><math display="inline" style="text-indent: 0em;" xmlns="http://www.w3.org/1998/Math/MathML"><mi>k</mi></math>,
      что можно расставить корабли, как описано в условии. 
   </div>
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
            <td><pre>7
</pre></td>
            <td><pre>2
</pre></td>
         </tr>
      </tbody>
   </table>
   <h2>Примечания</h2>
   <div class="notes"> Пояснение к примеру: для поля <!--l. 56--><math display="inline" style="text-indent: 0em;" xmlns="http://www.w3.org/1998/Math/MathML"><mn>1</mn>
      <mo>×</mo> <mn>7</mn></math> ответ равен 2. Расставить один корабль размера <!--l. 56--><math display="inline" style="text-indent:
      0em;" xmlns="http://www.w3.org/1998/Math/MathML"><mn>1</mn> <mo>×</mo> <mn>2</mn></math> и два корабля размера <!--l. 56--><math
      display="inline" style="text-indent: 0em;" xmlns="http://www.w3.org/1998/Math/MathML"><mn>1</mn> <mo>×</mo> <mn>1</mn></math>
      можно следующим образом: <div style="margin-left: 1em; margin-right: 1em; text-align: center;">
      <!--l. 57-->
      <p style="text-indent: 0em;">
      <!--l. 58-->
      </p><p style="text-indent: 0em;"><img alt="PIC" src="https://contest.yandex.ru/testsys/statement-image?imageId=8571481bcbced5361a26b4259f07da99308747d8db9f6c3e6a84ff9641606084"></p>
      <p></p>
      </div>
      
   </div>
