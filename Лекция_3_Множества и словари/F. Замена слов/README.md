<div class="problem-statement">
   <div class="header">
      <h1 class="title">F. Замена слов</h1>
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
   <div class="legend"><span style="">
         <p>С целью экономии чернил в картридже принтера было принято решение укоротить некоторые слова в тексте. Для этого был составлен
            словарь слов, до которых можно сокращать более длинные слова. Слово из текста можно сократить, если в словаре найдется слово,
            являющееся началом слова из текста. Например, если в списке есть слово "лом", то слова из текста "ломбард", "ломоносов" и
            другие слова, начинающиеся на "лом", можно сократить до "лом".
         </p></span><p>Если слово из текста можно сократить до нескольких слов из словаря, то следует сокращать его до самого короткого слова.</p>
   </div>
   <h2>Формат ввода</h2>
   <div class="input-specification"><span style="">
         <p>В первой строке через пробел вводятся слова из словаря, слова состоят из маленьких латинских букв. Гарантируется, что словарь
            не пуст и количество слов в словаре не превышет 1000, а длина слов&nbsp;&mdash; 100 символов.
         </p></span><p>Во второй строке через пробел вводятся слова текста (они также состоят только из маленьких латинских букв). Количество слов
         в тексте не превосходит <span class="tex-math-text">10<sup>5</sup></span>, а суммарное количество букв в них&nbsp;&mdash; <span class="tex-math-text">10<sup>6</sup></span>.
      </p>
   </div>
   <h2>Формат вывода</h2>
   <div class="output-specification"><span style="">
         <p>Выведите текст, в котором осуществлены замены.</p></span></div>
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
            <td><pre>a b
abdafb basrt casds dsasa a</pre></td>
            <td><pre>a b casds dsasa a
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
            <td><pre>aa bc aaa
a aa aaa bcd abcd
</pre></td>
            <td><pre>a aa aa bc abcd
</pre></td>
         </tr>
      </tbody>
   </table>