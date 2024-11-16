<div class="problem-statement">
   <div class="header">
      <h1 class="title">E. Прибыльный стартап</h1>
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
   <div class="legend">
      <!--l. 47--><math display="inline" style="text-indent: 0em;" xmlns="http://www.w3.org/1998/Math/MathML"><mi>k</mi></math>
      друзей организовали стартап по производству укулеле для кошек. На сегодняшний день прибыль составила <!--l. 47--><math display="inline"
      style="text-indent: 0em;" xmlns="http://www.w3.org/1998/Math/MathML"><mi>n</mi></math> рублей. Вы, как главный бухгалтер компании,
      хотите в каждый из ближайших <!--l. 47--><math display="inline" style="text-indent: 0em;" xmlns="http://www.w3.org/1998/Math/MathML"><mi>d</mi></math>
      дней приписывать по одной цифре в конец числа, выражающего прибыль. При этом в каждый из дней прибыль должна делиться на <!--l.
      47--><math display="inline" style="text-indent: 0em;" xmlns="http://www.w3.org/1998/Math/MathML"><mi>k</mi></math>. 
   </div>
   <h2>Формат ввода</h2>
   <div class="input-specification"> В единственной строке входных данных через пробел записаны три числа: <!--l. 50--><math display="inline" style="text-indent:
      0em;" xmlns="http://www.w3.org/1998/Math/MathML"><mi>n</mi><mo>,</mo><mi>k</mi><mo>,</mo><mi>d</mi></math> — изначальная прибыль,
      количество учредителей компании и количество дней, которое вы собираетесь следить за прибылью <!--l. 50--><math display="inline"
      style="text-indent: 0em;" xmlns="http://www.w3.org/1998/Math/MathML"><mrow><mo>(</mo><mrow><mn>1</mn> <mo>≤</mo> <mi>n</mi><mo>,</mo><mi>k</mi>
      <mo>≤</mo> <mn>1</mn><msup><mrow><mn>0</mn></mrow><mrow><mn>9</mn></mrow></msup><mo>,</mo><mn>1</mn> <mo>≤</mo> <mi>d</mi>
      <mo>≤</mo> <mn>1</mn><msup><mrow><mn>0</mn></mrow><mrow><mn>5</mn></mrow></msup></mrow><mo>)</mo></mrow></math>. <span style="font-weight:
      bold;">НЕ</span> гарантируется, что <!--l. 50--><math display="inline" style="text-indent: 0em;" xmlns="http://www.w3.org/1998/Math/MathML"><mi>n</mi></math>
      делится на <!--l. 50--><math display="inline" style="text-indent: 0em;" xmlns="http://www.w3.org/1998/Math/MathML"><mi>k</mi></math>.
      
   </div>
   <h2>Формат вывода</h2>
   <div class="output-specification"> Выведите одно целое число <!--l. 53--><math display="inline" style="text-indent: 0em;" xmlns="http://www.w3.org/1998/Math/MathML"><mi>x</mi></math>&nbsp;—
      прибыль компании через <!--l. 53--><math display="inline" style="text-indent: 0em;" xmlns="http://www.w3.org/1998/Math/MathML"><mi>d</mi></math>
      дней. Первые цифры числа <!--l. 53--><math display="inline" style="text-indent: 0em;" xmlns="http://www.w3.org/1998/Math/MathML"><mi>x</mi></math>
      должны совпадать с числом <!--l. 53--><math display="inline" style="text-indent: 0em;" xmlns="http://www.w3.org/1998/Math/MathML"><mi>n</mi></math>.
      Все префиксы числа <!--l. 53--><math display="inline" style="text-indent: 0em;" xmlns="http://www.w3.org/1998/Math/MathML"><mi>x</mi></math>,
      которые длиннее числа <!--l. 53--><math display="inline" style="text-indent: 0em;" xmlns="http://www.w3.org/1998/Math/MathML"><mi>n</mi></math>
      на <!--l. 53--><math display="inline" style="text-indent: 0em;" xmlns="http://www.w3.org/1998/Math/MathML"><mn>1</mn><mo>,</mo><mn>2</mn><mo>,</mo><mo>…</mo><mo>,</mo><mi>d</mi></math>
      цифр, должны делиться на <!--l. 53--><math display="inline" style="text-indent: 0em;" xmlns="http://www.w3.org/1998/Math/MathML"><mi>k</mi></math>.
      Если возможных ответов несколько, выведите любой из них. Если ответа не существует, выведите <!--l. 53--><math display="inline"
      style="text-indent: 0em;" xmlns="http://www.w3.org/1998/Math/MathML"> <mo>−</mo> <mn>1</mn></math>. 
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
            <td><pre>21 108 1
</pre></td>
            <td><pre>216
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
            <td><pre>5 12 4
</pre></td>
            <td><pre>-1
</pre></td>
         </tr>
      </tbody>
   </table>
   <h2>Примечания</h2>
   <div class="notes"> В первом тестовом примере всего один день нужно следить за прибылью. Можно дописать цифру <!--l. 56--><math display="inline"
      style="text-indent: 0em;" xmlns="http://www.w3.org/1998/Math/MathML"><mn>6</mn></math> в конец числа <!--l. 56--><math display="inline"
      style="text-indent: 0em;" xmlns="http://www.w3.org/1998/Math/MathML"><mn>2</mn><mn>1</mn></math> и получить прибыль, делящуюся
      на <!--l. 56--><math display="inline" style="text-indent: 0em;" xmlns="http://www.w3.org/1998/Math/MathML"><mn>1</mn><mn>0</mn><mn>8</mn></math>.
      <!--l. 58-->
      <p style="text-indent: 0em;">Во втором тестовом примере мы в первый же день не можем получить прибыль, делящуюся на <!--l.
      58--><math display="inline" style="text-indent: 0em;" xmlns="http://www.w3.org/1998/Math/MathML"><mi>k</mi></math>, какая
      бы цифра не была дописана у числу <!--l. 58--><math display="inline" style="text-indent: 0em;" xmlns="http://www.w3.org/1998/Math/MathML"><mi>n</mi></math>,
      поэтому ответа не существует. </p>
      
   </div>