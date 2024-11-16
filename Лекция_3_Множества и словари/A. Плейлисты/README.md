<div class="problem-statement">
   <div class="header">
      <h1 class="title">A. Плейлисты</h1>
      <table>
         <tr class="time-limit">
            <td class="property-title">Ограничение времени</td>
            <td>1.5&nbsp;секунд</td>
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
   <div class="legend"> Костя успешно прошел собеседование и попал на стажировку в отдел разработки сервиса «Музыка». <!--l. 49-->
      <p style="text-indent: 0em;">Конкретно ему поручили такое задание — научиться подбирать плейлист для группы друзей, родственников
      или коллег. При этом нужно подобрать такой плейлист, в который входят исключительно нравящиеся всем членам группы песни. <!--l.
      51-->
      </p><p style="text-indent: 0em;">Костя очень хотел выполнить это задание быстро и качественно, но у него не получается. Помогите
      ему написать программу, которая составляет плейлист для группы людей. </p>
      <p></p>
      
   </div>
   <h2>Формат ввода</h2>
   <div class="input-specification"> В первой строке расположено одно натуральное число <!--l. 54--><math display="inline" style="text-indent: 0em;" xmlns="http://www.w3.org/1998/Math/MathML"><mi>n</mi></math><!--l.
      54--><math display="inline" style="text-indent: 0em;" xmlns="http://www.w3.org/1998/Math/MathML"><mrow><mo>(</mo><mrow><mn>1</mn>
      <mo>≤</mo> <mi>n</mi> <mo>≤</mo> <mn>2</mn> <mo>⋅</mo> <mn>1</mn><msup><mrow><mn>0</mn></mrow><mrow><mn>5</mn></mrow></msup></mrow><mo>)</mo></mrow></math>,
      где <!--l. 54--><math display="inline" style="text-indent: 0em;" xmlns="http://www.w3.org/1998/Math/MathML"><mi>n</mi></math>
      – количество человек в группе. <!--l. 56-->
      <p style="text-indent: 0em;">В следующих <!--l. 56--><math display="inline" style="text-indent: 0em;" xmlns="http://www.w3.org/1998/Math/MathML"><mn>2</mn>
      <mo>⋅</mo> <mi>n</mi></math> строках идет описание любимых плейлистов членов группы. По <!--l. 56--><math display="inline"
      style="text-indent: 0em;" xmlns="http://www.w3.org/1998/Math/MathML"><mn>2</mn></math> строки на каждого участника. <!--l.
      58-->
      </p><p style="text-indent: 0em;">В первой из этих <!--l. 58--><math display="inline" style="text-indent: 0em;" xmlns="http://www.w3.org/1998/Math/MathML"><mn>2</mn></math>-х
      строк расположено число <!--l. 58--><math display="inline" style="text-indent: 0em;" xmlns="http://www.w3.org/1998/Math/MathML"><msub><mrow><mi>k</mi></mrow><mrow><mi>i</mi></mrow></msub></math>
      — количество любимых треков <!--l. 58--><math display="inline" style="text-indent: 0em;" xmlns="http://www.w3.org/1998/Math/MathML"><mi>i</mi></math>-го
      члена группы. В следующей строке расположено <!--l. 58--><math display="inline" style="text-indent: 0em;" xmlns="http://www.w3.org/1998/Math/MathML"><msub><mrow><mi>k</mi></mrow><mrow><mi>i</mi></mrow></msub></math>
      строк через пробел — названия любимых треков <!--l. 58--><math display="inline" style="text-indent: 0em;" xmlns="http://www.w3.org/1998/Math/MathML"><mi>i</mi></math>-го
      участника группы. <!--l. 60-->
      </p><p style="text-indent: 0em;">Каждый трек в плейлисте задан в виде строки, все строки уникальны, сумма длин строк не превосходит
      <!--l. 60--><math display="inline" style="text-indent: 0em;" xmlns="http://www.w3.org/1998/Math/MathML"><mn>2</mn> <mo>⋅</mo>
      <mn>1</mn><msup><mrow><mn>0</mn></mrow><mrow><mn>6</mn></mrow></msup></math>. Строки содержат большие и маленькие латинские
      буквы и цифры. </p>
      <p></p>
      <p></p>
      
   </div>
   <h2>Формат вывода</h2>
   <div class="output-specification"> Выведите количество, а затем сам список песен через пробел — список треков, которые нравятся каждому участнику группы. Ответ
      необходимо <span style="font-weight: bold;">отсортировать </span>в лексикографическом порядке! 
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
            <td><pre>1
2
GoGetIt Life
</pre></td>
            <td><pre>2
GoGetIt Life 
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
2
Love Life
2
Life GoodDay
</pre></td>
            <td><pre>1
Life 
</pre></td>
         </tr>
      </tbody>
   </table>
</div>