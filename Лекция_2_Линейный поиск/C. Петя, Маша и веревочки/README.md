<div class="problem-statement">
   <div class="header">
      <h1 class="title">C. Петя, Маша и верёвочки</h1>
      <table>
         <tr class="time-limit">
            <td class="property-title">Ограничение времени</td>
            <td>1&nbsp;секунда</td>
         </tr>
         <tr class="memory-limit">
            <td class="property-title">Ограничение памяти</td>
            <td>512Mb</td>
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
         <p>На столе лежали две одинаковые верёвочки целой положительной длины. </p></span><p>Петя разрезал одну из верёвочек на <span class="tex-math-text">N</span> частей, каждая из которых имеет целую положительную длину, так что на столе стало <span class="tex-math-text">N+1</span> верёвочек. Затем в комнату зашла Маша и взяла одну из лежащих на столе верёвочек. По длинам оставшихся на столе <span class="tex-math-text">N</span> верёвочек определите, какую <span style="font-weight:bold;">наименьшую</span> длину может иметь верёвочка, взятая Машей.
      </p>
   </div>
   <h2>Формат ввода</h2>
   <div class="input-specification"><span style="">
         <p>Первая строка входных данных содержит одно целое число <span class="tex-math-text">N</span> &mdash; количество верёвочек, оставшихся на столе (<span class="tex-math-text">2 &le; N &le; 1000</span>). Во второй строке содержится <span class="tex-math-text">N</span> целых чисел <span class="tex-math-text">l<sub>i</sub></span> &mdash; длины верёвочек (<span class="tex-math-text">1 &le; l<sub>i</sub> &le; 1000</span>).
         </p></span></div>
   <h2>Формат вывода</h2>
   <div class="output-specification"><span style="">
         <p>Выведите одно целое число &mdash; наименьшую длину, которую может иметь верёвочка, взятая Машей.</p></span></div>
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
            <td><pre>4
1 5 2 1
</pre></td>
            <td><pre>1
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
            <td><pre>4
5 12 4 3
</pre></td>
            <td><pre>24
</pre></td>
         </tr>
      </tbody>
   </table>
</div>