<div class="problem-statement">
   <div class="header">
      <h1 class="title">J. Два прямоугольника</h1>
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
         <p>Недавно один известный художник-абстракционист произвел на свет новый шедевр &mdash; картину &laquo;Два черных непересекающихся прямоугольника&raquo;. Картина представляет собой прямоугольник <span class="tex-math-text">m&times; n</span>, разбитый на квадраты <span class="tex-math-text">1&times; 1</span>, некоторые из которых закрашены любимым цветом автора &mdash; черным. Федя &mdash; не любитель абстрактных картин, однако ему стало интересно, действительно ли на картине изображены два непересекающихся прямоугольника.
            Помогите ему это узнать. Прямоугольники не пересекаются в том смысле, что они не имеют общих клеток. 
         </p></span></div>
   <h2>Формат ввода</h2>
   <div class="input-specification"><span style="">
         <p>Первая строка входного файла содержит числа <span class="tex-math-text">m</span> и <span class="tex-math-text">n</span> (<span class="tex-math-text">1 &le; m, n &le; 200</span>). Следующие <span class="tex-math-text">m</span> строк содержат описание рисунка. Каждая строка содержит ровно <span class="tex-math-text">n</span> символов. Символ&nbsp;&laquo;.&raquo; обозначает пустой квадрат, а символ&nbsp;&laquo;#&raquo; &mdash; закрашенный.
         </p></span></div>
   <h2>Формат вывода</h2>
   <div class="output-specification"><span style="">
         <p>Если рисунок можно представить как два непересекающихся прямоугольника, выведите в первой строке &laquo;YES&raquo;, а в следующих <span class="tex-math-text">m</span> строках выведите рисунок в том же виде, в каком он задан во входном файле, заменив квадраты, соответствующие первому прямоугольнику
            на символ &laquo;a&raquo;, а второму &mdash; на символ &laquo;b&raquo;. Если решений несколько, выведите любое. 
         </p></span><p>Если же этого сделать нельзя, выведите в выходной файл &laquo;NO&raquo;.</p>
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
            <td><pre>2 1
#
.
</pre></td>
            <td><pre>NO
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
            <td><pre>2 2
..
##
</pre></td>
            <td><pre>YES
..
ab
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
            <td><pre>1 3
###
</pre></td>
            <td><pre>YES
abb
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
            <td><pre>1 5
####.
</pre></td>
            <td><pre>YES
abbb.
</pre></td>
         </tr>
      </tbody>
   </table>
</div>