<div class="problem-statement">
   <div class="header">
      <h1 class="title">E. Нумерация дробей</h1>
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
   <div class="legend"><span style="">
         <p>Георг Кантор доказал, что множество всех рациональных чисел счетно (т.е. все рациональные числа можно пронумеровать).</p></span><p>Чтобы упорядочить дроби необходимо их положить в таблицу, как показано на рисунке. В строку с номером <span class="tex-math-text">i</span> этой матрицы по порядку записаны дроби с числителем <span class="tex-math-text">i</span>, а в столбец с номером <span class="tex-math-text">j</span> дроби с знаменателем <span class="tex-math-text">j</span>.
      </p>
      <p><img class="user-image" src="/testsys/statement-image?imageId=3cc21750b8e8a181a72a5c418e33d8dbfb560a6d294bac8db573eeb3958595a9"></p>
      <p>Дальше необходимо выписать все дроби в том порядке, как показано на рисунке стрелками. Получится такая последовательность:&nbsp;<span class="tex-math-inline"><img class="tex-math" src="/testsys/tex/render/XGZyYWN7MX17MX0=.png"></span>,&nbsp;<span class="tex-math-inline"><img class="tex-math" src="/testsys/tex/render/XGZyYWN7Mn17MX0=.png"></span>,&nbsp;<span class="tex-math-inline"><img class="tex-math" src="/testsys/tex/render/XGZyYWN7MX17Mn0=.png"></span>,&nbsp;<span class="tex-math-inline"><img class="tex-math" src="/testsys/tex/render/XGZyYWN7MX17M30=.png"></span>,&nbsp;<span class="tex-math-inline"><img class="tex-math" src="/testsys/tex/render/XGZyYWN7Mn17Mn0=.png"></span>,&nbsp;<span class="tex-math-inline"><img class="tex-math" src="/testsys/tex/render/XGZyYWN7M317MX0=.png"></span>,&nbsp;<span class="tex-math-text">&hellip;</span></p>
      <p>Вам требуется по числу <span class="tex-math-text">n</span> найти числитель и знаменатель <span class="tex-math-text">n</span>-ой дроби.
      </p>
      <p></p>
   </div>
   <h2>Формат ввода</h2>
   <div class="input-specification"><span style="">
         <p>Во входном файле дано число <span class="tex-math-text">n</span> (<span class="tex-math-text">1 &le; n &le; 10<sup>18</sup></span>)&nbsp;&mdash; порядковый номер дроби в последовательности. 
         </p></span></div>
   <h2>Формат вывода</h2>
   <div class="output-specification"><span style="">
         <p>В выходной файл требуется вывести через символ <span class="tex-monospace">/</span> два числа: числитель и знаменатель соответствующей дроби. 
         </p></span></div>
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
</pre></td>
            <td><pre>1/1</pre></td>
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
            <td><pre>6
</pre></td>
            <td><pre>3/1</pre></td>
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
            <td><pre>2
</pre></td>
            <td><pre>2/1</pre></td>
         </tr>
      </tbody>
   </table>