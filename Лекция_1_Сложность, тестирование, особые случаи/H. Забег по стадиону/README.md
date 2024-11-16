<div class="problem-statement">
   <div class="header">
      <h1 class="title">H. Забег по стадиону</h1>
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
   <div class="legend"> Стадион представляет собой окружность <span style="font-weight: bold;">длиной</span><!--l. 47--><math display="inline" style="text-indent:
      0em;" xmlns="http://www.w3.org/1998/Math/MathML"><mi>L</mi></math> метров, на которой отмечена точка старта. По стадиону бегают
      Кирилл и Антон. У каждого мальчика есть своя точка старта (она представляет собой расстояние в метрах от старта, отсчитанное
      по часовой стрелке) и своя скорость в метрах в секунду (положительная скорость означает, что мальчик бежит по часовой стрелке,
      отрицательная&nbsp;— что бежит против часовой, а нулевая&nbsp;— что он стоит на месте). <!--l. 49-->
      <p style="text-indent: 0em;">Вам нужно сказать, через какое минимальное время мальчики окажутся на одинаковом расстоянии от
      точки старта. Обратите внимание, что в этот момент они могли находиться в разных точках. Расстоянием от точки <!--l. 49--><math
      display="inline" style="text-indent: 0em;" xmlns="http://www.w3.org/1998/Math/MathML"><mi>A</mi></math> до точки <!--l. 49--><math
      display="inline" style="text-indent: 0em;" xmlns="http://www.w3.org/1998/Math/MathML"><mi>B</mi></math> называется минимальное
      из расстояний, которое нужно пробежать из точки <!--l. 49--><math display="inline" style="text-indent: 0em;" xmlns="http://www.w3.org/1998/Math/MathML"><mi>A</mi></math>
      по или против часовой стрелки, чтобы оказаться в <!--l. 49--><math display="inline" style="text-indent: 0em;" xmlns="http://www.w3.org/1998/Math/MathML"><mi>B</mi></math>.
      </p>
      
   </div>
   <h2>Формат ввода</h2>
   <div class="input-specification"> В единственной строке вводится <!--l. 52--><math display="inline" style="text-indent: 0em;" xmlns="http://www.w3.org/1998/Math/MathML"><mn>5</mn></math>
      целых чисел <!--l. 52--><math display="inline" style="text-indent: 0em;" xmlns="http://www.w3.org/1998/Math/MathML"><mi>L</mi><mo>,</mo><msub><mrow><mi>x</mi></mrow><mrow><mn>1</mn></mrow></msub><mo>,</mo><msub><mrow><mi>v</mi></mrow><mrow><mn>1</mn></mrow></msub><mo>,</mo><msub><mrow><mi>x</mi></mrow><mrow><mn>2</mn></mrow></msub><mo>,</mo><msub><mrow><mi>v</mi></mrow><mrow><mn>2</mn></mrow></msub></math>
      (<!--l. 52--><math display="inline" style="text-indent: 0em;" xmlns="http://www.w3.org/1998/Math/MathML"><mn>1</mn> <mo>≤</mo>
      <mi>L</mi> <mo>≤</mo> <mn>1</mn><msup><mrow><mn>0</mn></mrow><mrow><mn>9</mn></mrow></msup></math>, <!--l. 52--><math display="inline"
      style="text-indent: 0em;" xmlns="http://www.w3.org/1998/Math/MathML"><mn>0</mn> <mo>≤</mo> <msub><mrow><mi>x</mi></mrow><mrow><mn>1</mn></mrow></msub><mo>,</mo><msub><mrow><mi>x</mi></mrow><mrow><mn>2</mn></mrow></msub>
      <mo>&lt;</mo> <mi>L</mi></math>, <!--l. 52--><math display="inline" style="text-indent: 0em;" xmlns="http://www.w3.org/1998/Math/MathML"><mo>|</mo><msub><mrow><mi>v</mi></mrow><mrow><mn>1</mn></mrow></msub><mo>|</mo><mo>,</mo><mo>|</mo><msub><mrow><mi>v</mi></mrow><mrow><mn>2</mn></mrow></msub><mo>|</mo><mo>≤</mo>
      <mn>1</mn><msup><mrow><mn>0</mn></mrow><mrow><mn>9</mn></mrow></msup></math>)&nbsp;— длины стадиона в метрах, начальная точка
      Кирилла, скорость Кирилла, начальная точка Антона, скорость Антона. 
   </div>
   <h2>Формат вывода</h2>
   <div class="output-specification"> В первой строке выведите слово «YES», если случится момент, когда мальчики будут на одинаковом расстоянии от старта, или
      «NO», если такого момента не произойдёт. <!--l. 57-->
      <p style="text-indent: 0em;">Если ответ «YES», то во второй строке выведите одно вещественное число&nbsp;— через какое минимальное
      количество времени мальчики окажутся на одинаковом расстоянии от старта. <!--l. 59-->
      </p><p style="text-indent: 0em;">Вы можете выводить каждую букву в любом регистре (строчную или заглавную). Например, строки
      «<span style="font-family: monospace;">yEs</span>», «<span style="font-family: monospace;">yes</span>», «<span style="font-family:
      monospace;">Yes</span>» и «<span style="font-family: monospace;">YES</span>» будут приняты как положительный ответ. <!--l.
      61-->
      </p><p style="text-indent: 0em;">Ваш ответ будет считаться правильным, если его абсолютная или относительная ошибка не превосходит
      <!--l. 61--><math display="inline" style="text-indent: 0em;" xmlns="http://www.w3.org/1998/Math/MathML"><mn>1</mn><msup><mrow><mn>0</mn></mrow><mrow><mo>−</mo><mn>9</mn></mrow></msup></math>.
      <!--l. 63-->
      </p><p style="text-indent: 0em;">Формально, пусть ваш ответ равен <!--l. 63--><math display="inline" style="text-indent: 0em;"
      xmlns="http://www.w3.org/1998/Math/MathML"><mi>a</mi></math>, а ответ жюри равен <!--l. 63--><math display="inline" style="text-indent:
      0em;" xmlns="http://www.w3.org/1998/Math/MathML"><mi>b</mi></math>. Ваш ответ будет зачтен, если и только если <!--l. 63--><math
      display="inline" style="text-indent: 0em;" xmlns="http://www.w3.org/1998/Math/MathML"> <mfrac><mrow><mo>|</mo><mi>a</mi><mo>−</mo><mi>b</mi><mo>|</mo></mrow>
      <mrow><mo> max</mo> <mrow><mo>(</mo><mrow><mn>1</mn><mo>,</mo><mo>|</mo><mi>b</mi><mo>|</mo></mrow><mo>)</mo></mrow></mrow></mfrac>
      <mo>≤</mo> <mn>1</mn><msup><mrow><mn>0</mn></mrow><mrow><mo>−</mo><mn>9</mn></mrow></msup></math>. </p>
      <p></p>
      <p></p>
      <p></p>
      
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
            <td><pre>6 3 1 1 1
</pre></td>
            <td><pre>YES
1.0000000000
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
            <td><pre>12 8 10 5 20
</pre></td>
            <td><pre>YES
0.3000000000
</pre></td>
         </tr>
      </tbody>
   </table>
   <h3>Пример 3</h3>
   <table class="sample-tests">
      <thead>
         <tr>
            <th>Ввод</th>
            <th>Вывод</th>
         </tr>
      </thead>
      <tbody>
         <tr>
            <td><pre>5 0 0 1 2
</pre></td>
            <td><pre>YES
2.0000000000
</pre></td>
         </tr>
      </tbody>
   </table>
   <h3>Пример 4</h3>
   <table class="sample-tests">
      <thead>
         <tr>
            <th>Ввод</th>
            <th>Вывод</th>
         </tr>
      </thead>
      <tbody>
         <tr>
            <td><pre>10 7 -3 1 4
</pre></td>
            <td><pre>YES
0.8571428571
</pre></td>
         </tr>
      </tbody>
   </table>
   <h2>Примечания</h2>
   <div class="notes"> В первом тесте Кирилл изначально находится в точке <!--l. 66--><math display="inline" style="text-indent: 0em;" xmlns="http://www.w3.org/1998/Math/MathML"><mn>3</mn></math>
      и бежит по часовой стрелке со скоростью <!--l. 66--><math display="inline" style="text-indent: 0em;" xmlns="http://www.w3.org/1998/Math/MathML"><mn>1</mn></math>.
      Антон находится в точке <!--l. 66--><math display="inline" style="text-indent: 0em;" xmlns="http://www.w3.org/1998/Math/MathML"><mn>1</mn></math>
      и также бежит по часовой стрелке со скоростью <!--l. 66--><math display="inline" style="text-indent: 0em;" xmlns="http://www.w3.org/1998/Math/MathML"><mn>1</mn></math>.
      Через <!--l. 66--><math display="inline" style="text-indent: 0em;" xmlns="http://www.w3.org/1998/Math/MathML"><mn>1</mn></math>
      секунду мальчики окажутся в точках <!--l. 66--><math display="inline" style="text-indent: 0em;" xmlns="http://www.w3.org/1998/Math/MathML"><mn>4</mn></math>
      и <!--l. 66--><math display="inline" style="text-indent: 0em;" xmlns="http://www.w3.org/1998/Math/MathML"><mn>2</mn></math>
      соответственно. Обе эти точки расположены на расстоянии <!--l. 66--><math display="inline" style="text-indent: 0em;" xmlns="http://www.w3.org/1998/Math/MathML"><mn>2</mn></math>
      метра от старта (точки <!--l. 66--><math display="inline" style="text-indent: 0em;" xmlns="http://www.w3.org/1998/Math/MathML"><mn>0</mn></math>,
      совпадающей с точкой <!--l. 66--><math display="inline" style="text-indent: 0em;" xmlns="http://www.w3.org/1998/Math/MathML"><mn>6</mn></math>).
      Можно показать, что до этого они всегда находились на разном расстоянии от старта. Значит, ответ&nbsp;— <!--l. 66--><math
      display="inline" style="text-indent: 0em;" xmlns="http://www.w3.org/1998/Math/MathML"><mn>1</mn></math>. <!--l. 68-->
      <p style="text-indent: 0em;">Во втором тесте оба мальчика окажутся в точке <!--l. 68--><math display="inline" style="text-indent:
      0em;" xmlns="http://www.w3.org/1998/Math/MathML"><mn>1</mn><mn>1</mn></math> через <!--l. 68--><math display="inline" style="text-indent:
      0em;" xmlns="http://www.w3.org/1998/Math/MathML"><mn>0</mn><mo>.</mo><mn>3</mn></math> секунды. <!--l. 70-->
      </p><p style="text-indent: 0em;">В третьем Антон прибежит к Кириллу в точку <!--l. 70--><math display="inline" style="text-indent:
      0em;" xmlns="http://www.w3.org/1998/Math/MathML"><mn>0</mn></math> за <!--l. 70--><math display="inline" style="text-indent:
      0em;" xmlns="http://www.w3.org/1998/Math/MathML"><mn>2</mn></math> секунды. </p>
      <p></p>
      
   </div>