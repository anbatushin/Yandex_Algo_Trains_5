<div class="problem-statement">
   <div class="header">
      <h1 class="title">G. Ни больше ни меньше</h1>
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
         <p>Дан массив целых положительных чисел <span class="tex-math-text">a</span> длины <span class="tex-math-text">n</span>. Разбейте его на <span style="font-weight:bold;">минимально возможное</span> количество отрезков, чтобы каждое число было не меньше длины отрезка которому оно принадлежит. Длиной отрезка считается количество
            чисел в нем.
         </p></span><p>Разбиение массива на отрезки считается корректным, если каждый элемент принадлежит ровно одному отрезку.</p>
   </div>
   <h2>Формат ввода</h2>
   <div class="input-specification"><span style="">
         <p>Первая строка содержит одно целое число <span class="tex-math-text">t</span> <span class="tex-math-text">(1 &le; t &le; 1&#8239;000)</span> &mdash; количество наборов тестовых данных. Затем следуют <span class="tex-math-text">t</span> наборов тестовых данных.
         </p></span><p>Первая строка набора тестовых данных содержит одно целое число <span class="tex-math-text">n</span> <span class="tex-math-text">(1 &le; n &le; 10<sup>5</sup>)</span> &mdash; длину массива.
      </p>
      <p>Следующая строка содержит <span class="tex-math-text">n</span> целых чисел <span class="tex-math-text">a<sub>1</sub>, a<sub>2</sub>, &hellip;, a<sub>n</sub></span> <span class="tex-math-text">(1 &le; a<sub>i</sub> &le; n)</span> &mdash; массив <span class="tex-math-text">a</span>.
      </p>
      <p>Гарантируется, что сумма <span class="tex-math-text">n</span> по всем наборам тестовых данных не превосходит <span class="tex-math-text">2 &#x22C5; 10<sup>5</sup></span>.
      </p>
   </div>
   <h2>Формат вывода</h2>
   <div class="output-specification"><span style="">
         <p>Для каждого набора тестовых данных в первой строке выведите число <span class="tex-math-text">k</span> &mdash; количество отрезков в вашем разбиении.
         </p></span><p>Затем в следующей строке выведите <span class="tex-math-text">k</span> чисел <span class="tex-math-text">len<sub>1</sub>, len<sub>2</sub>, &hellip;, len<sub>k</sub></span> <span class="tex-math-inline"><img class="tex-math" src="https://contest.yandex.ru/testsys/tex/render/KDEgXGxlcSBsZW5faSBcbGVxIG4sXCBcc3VtXGxpbWl0c197aSA9IDF9XntrfWxlbl9pID0gbik=.png"></span> &mdash; длины отрезков в порядке слева направо.
      </p>
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
            <td><pre>3
5
1 3 3 3 2
16
1 9 8 7 6 7 8 9 9 9 9 9 9 9 9 9
7
7 2 3 4 3 2 7
</pre></td>
            <td><pre>3
1 2 2
3
1 6 9 
3
2 3 2 
</pre></td>
         </tr>
      </tbody>
   </table>
   <h2>Примечания</h2>
   <div class="notes"><span style="">
         <p>Ответы в примере соответствуют разбиениям:</p></span><p><span class="tex-math-text">{[1], [3, 3], [3, 2]}</span></p>
      <p><span class="tex-math-text">{[1], [9, 8, 7, 6, 7, 8], [9, 9, 9, 9, 9, 9, 9, 9, 9]}</span></p>
      <p><span class="tex-math-text">{[7, 2], [3, 4, 3], [2, 7]}</span></p>
      <p>В первом наборе тестовых данных набор длин <span class="tex-math-text">{1, 3, 1}</span>, соответствующий разбиению <span class="tex-math-text">{[1], [3, 3, 3], [2]}</span>, также был бы корректным.
      </p>
   </div>
