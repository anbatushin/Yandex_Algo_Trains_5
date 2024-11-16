<div class="problem-statement">
   <div class="header">
      <h1 class="title">F. Велодорожки</h1>
      <table>
         <tr class="time-limit">
            <td class="property-title">Ограничение времени</td>
            <td>4&nbsp;секунды</td>
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
   <div class="legend"> Мэр одного города очень любит следить за тенденциями и воспроизводить их в своём городе. До него дошла новость о популярности
      велодорожек. Теперь он хочет проложить велодорожки в своём городе и сделать это лучше, чем в других городах! Поэтому он решил
      сделать велодорожки даже на главной площади города. <!--l. 49-->
      <p style="text-indent: 0em;">Главная площадь представляет собой прямоугольник шириной <!--l. 49--><math display="inline" style="text-indent:
      0em;" xmlns="http://www.w3.org/1998/Math/MathML"><mi>w</mi></math> и высотой <!--l. 49--><math display="inline" style="text-indent:
      0em;" xmlns="http://www.w3.org/1998/Math/MathML"><mi>h</mi></math>, замощённый квадратными плитками со стороной <!--l. 49--><math
      display="inline" style="text-indent: 0em;" xmlns="http://www.w3.org/1998/Math/MathML"><mn>1</mn></math>. Мэр хочет, чтобы
      было проложено две велодорожки <span style="font-weight: bold;">одинаковой ширины</span>: одна горизонтальная и одна вертикальная.
      К сожалению, ремонт на площади проводился достаточно давно и на некоторых плитках уже появились трещины. Мэр хочет проложить
      велодорожки так, чтобы после этого на площади остались только целые плитки. При строительстве велодорожек плитки на их месте
      убираются. Можно только убирать плитки с площади и нельзя менять местами или добавлять новые. Чтобы потратить меньше денег,
      мэр хочет сделать велодорожки наименьшей возможной ширины, при этом ширина дорожек должна быть целым числом. Определите, какой
      должна быть ширина велодорожек. </p>
      
   </div>
   <h2>Формат ввода</h2>
   <div class="input-specification"> В первой строке входных данных содержатся три целых числа <!--l. 52--><math display="inline" style="text-indent: 0em;" xmlns="http://www.w3.org/1998/Math/MathML"><mi>w</mi><mo>,</mo><mi>h</mi><mo>,</mo><mi>n</mi></math>
      (<!--l. 52--><math display="inline" style="text-indent: 0em;" xmlns="http://www.w3.org/1998/Math/MathML"><mn>1</mn> <mo>≤</mo>
      <mi>w</mi><mo>,</mo><mi>h</mi> <mo>≤</mo> <mn>1</mn><msup><mrow><mn>0</mn></mrow><mrow><mn>9</mn></mrow></msup></math>, <!--l.
      52--><math display="inline" style="text-indent: 0em;" xmlns="http://www.w3.org/1998/Math/MathML"><mn>1</mn> <mo>≤</mo> <mi>n</mi>
      <mo>≤</mo><mo> min</mo><mrow><mo>(</mo><mrow><mi>w</mi> <mo>×</mo> <mi>h</mi><mo>,</mo><mn>3</mn> <mo>⋅</mo> <mn>1</mn><msup><mrow><mn>0</mn></mrow><mrow><mn>5</mn></mrow></msup></mrow><mo>)</mo></mrow></math>)
      &nbsp;— ширина и высота площади и количество потрескавшихся плиток соответственно. <!--l. 54-->
      <p style="text-indent: 0em;">В следующих <!--l. 54--><math display="inline" style="text-indent: 0em;" xmlns="http://www.w3.org/1998/Math/MathML"><mi>n</mi></math>
      строках содержится по 2 целых числа <!--l. 54--><math display="inline" style="text-indent: 0em;" xmlns="http://www.w3.org/1998/Math/MathML"><msub><mrow><mi>x</mi></mrow><mrow><mi>i</mi></mrow></msub><mo>,</mo><msub><mrow><mi>y</mi></mrow><mrow><mi>i</mi></mrow></msub></math>
      (<!--l. 54--><math display="inline" style="text-indent: 0em;" xmlns="http://www.w3.org/1998/Math/MathML"><mn>1</mn> <mo>≤</mo>
      <msub><mrow><mi>x</mi></mrow><mrow><mi>i</mi></mrow></msub> <mo>≤</mo> <mi>w</mi></math>, <!--l. 54--><math display="inline"
      style="text-indent: 0em;" xmlns="http://www.w3.org/1998/Math/MathML"><mn>1</mn> <mo>≤</mo> <msub><mrow><mi>y</mi></mrow><mrow><mi>i</mi></mrow></msub>
      <mo>≤</mo> <mi>h</mi></math>) &nbsp;— координаты потрескавшихся плиток. <!--l. 54--><math display="inline" style="text-indent:
      0em;" xmlns="http://www.w3.org/1998/Math/MathML"><mrow><mo>(</mo><mrow><msub><mrow><mi>x</mi></mrow><mrow><mi>i</mi></mrow></msub><mo>,</mo><msub><mrow><mi>y</mi></mrow><mrow><mi>i</mi></mrow></msub></mrow><mo>)</mo></mrow><mo>≠</mo><mrow><mo>(</mo><mrow><msub><mrow><mi>x</mi></mrow><mrow><mi>j</mi></mrow></msub><mo>,</mo><msub><mrow><mi>y</mi></mrow><mrow><mi>j</mi></mrow></msub></mrow><mo>)</mo></mrow></math>
      при <!--l. 54--><math display="inline" style="text-indent: 0em;" xmlns="http://www.w3.org/1998/Math/MathML"><mi>i</mi><mo>≠</mo><mi>j</mi></math>.
      </p>
      
   </div>
   <h2>Формат вывода</h2>
   <div class="output-specification"> Выведите единственное число <!--l. 57--><math display="inline" style="text-indent: 0em;" xmlns="http://www.w3.org/1998/Math/MathML"><mi>c</mi></math>
      (<!--l. 57--><math display="inline" style="text-indent: 0em;" xmlns="http://www.w3.org/1998/Math/MathML"><mn>1</mn> <mo>≤</mo>
      <mi>c</mi> <mo>≤</mo><mo> min</mo><mrow><mo>(</mo><mrow><mi>w</mi><mo>,</mo><mi>h</mi></mrow><mo>)</mo></mrow></math>) &nbsp;—
      наименьшую возможную ширину велодорожек. 
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
            <td><pre>5 6 5
5 4
2 6
4 1
2 3
1 4
</pre></td>
            <td><pre>3
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
            <td><pre>4 3 4
1 1
4 3
4 1
1 3
</pre></td>
            <td><pre>3
</pre></td>
         </tr>
      </tbody>
   </table>
   <h2>Примечания</h2>
   <div class="notes"> Ниже приведены картинки к примерам из условия. Серым отмечены потрескавшиеся плитки. Во втором примере ширина дорожек равна
      меньшей из сторон прямоугольника. <div style="margin-left: 1em; margin-right: 1em; text-align: center;">
      <!--l. 62-->
      <p style="text-indent: 0em;">
      <!--l. 63-->
      </p><p style="text-indent: 0em;"><img alt="PIC" src="/testsys/statement-image?imageId=bcb7434301c02a4a5dea832a3d38b7de2d9b720fd9294bfc6fbbf564a9759242"></p>
      <p></p>
      </div>
      