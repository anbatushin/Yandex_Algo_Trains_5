<div class="problem-statement">
   <div class="header">
      <h1 class="title">A. Покраска деревьев</h1>
      <table>
         <tr class="time-limit">
            <td class="property-title">Ограничение времени</td>
            <td>1&nbsp;секунда</td>
         </tr>
         <tr class="memory-limit">
            <td class="property-title">Ограничение памяти</td>
            <td>64Mb</td>
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
   <div class="legend"> Вася и Маша участвуют в субботнике и красят стволы деревьев в белый цвет. Деревья растут вдоль улицы через равные промежутки
      в 1 метр. Одно из деревьев обозначено числом ноль, деревья по одну сторону занумерованы положительными числами <!--l. 47--><math
      display="inline" style="text-indent: 0em;" xmlns="http://www.w3.org/1998/Math/MathML"><mn>1</mn><mo>,</mo><mn>2</mn></math>
      и т.д., а в другую&nbsp;— отрицательными <!--l. 47--><math display="inline" style="text-indent: 0em;" xmlns="http://www.w3.org/1998/Math/MathML">
      <mo>−</mo> <mn>1</mn><mo>,</mo><mo>−</mo><mn>2</mn></math> и т.д. <!--l. 49-->
      <p style="text-indent: 0em;">Ведро с краской для Васи установили возле дерева <!--l. 49--><math display="inline" style="text-indent:
      0em;" xmlns="http://www.w3.org/1998/Math/MathML"><mi>P</mi></math>, а для Маши&nbsp;— возле дерева <!--l. 49--><math display="inline"
      style="text-indent: 0em;" xmlns="http://www.w3.org/1998/Math/MathML"><mi>Q</mi></math>. Ведра с краской очень тяжелые и Вася
      с Машей не могут их переставить, поэтому они окунают кисть в ведро и уже с этой кистью идут красить дерево. Краска на кисти
      из ведра Васи засыхает, когда он удаляется от ведра более чем на <!--l. 49--><math display="inline" style="text-indent: 0em;"
      xmlns="http://www.w3.org/1998/Math/MathML"><mi>V</mi> </math> метров, а из ведра Маши&nbsp;— на <!--l. 49--><math display="inline"
      style="text-indent: 0em;" xmlns="http://www.w3.org/1998/Math/MathML"><mi>M</mi></math> метров. Определите, сколько деревьев
      может быть покрашено. </p>
      
   </div>
   <h2>Формат ввода</h2>
   <div class="input-specification"> В первой строке содержится два целых числа <!--l. 52--><math display="inline" style="text-indent: 0em;" xmlns="http://www.w3.org/1998/Math/MathML"><mi>P</mi></math>
      и <!--l. 52--><math display="inline" style="text-indent: 0em;" xmlns="http://www.w3.org/1998/Math/MathML"><mi>V</mi> </math>&nbsp;—
      номер дерева, у которого стоит ведро Васи и на сколько деревьев он может от него удаляться. <!--l. 54-->
      <p style="text-indent: 0em;">В второй строке содержится два целых числа <!--l. 54--><math display="inline" style="text-indent:
      0em;" xmlns="http://www.w3.org/1998/Math/MathML"><mi>Q</mi></math> и <!--l. 54--><math display="inline" style="text-indent:
      0em;" xmlns="http://www.w3.org/1998/Math/MathML"><mi>M</mi></math>&nbsp;— аналогичные данные для Маши. <!--l. 56-->
      </p><p style="text-indent: 0em;">Все числа целые и по модулю не превосходят <!--l. 56--><math display="inline" style="text-indent:
      0em;" xmlns="http://www.w3.org/1998/Math/MathML"><mn>1</mn><msup><mrow><mn>0</mn></mrow><mrow><mn>8</mn></mrow></msup></math>.
      </p>
      <p></p>
      
   </div>
   <h2>Формат вывода</h2>
   <div class="output-specification"> Выведите одно число&nbsp;— количество деревьев, которые могут быть покрашены. </div>
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
            <td><pre>0 7
12 5
</pre></td>
            <td><pre>25
</pre></td>