  <main>
    <section class="registration">
      <h2>Message box</h2>
      <table name="inbox_table">
        <tr>
          <td>From</td>
          <td>Message content</td>
          <td>Recieved at</td>
        </tr>
        %a=0
        %for row in rows:
            <tr>
              %for col in row:
              <td>{{col}}</td>
              %end
            </tr>

          %a=a+1
        %end
      </table>
    </section>
  </main>
</body>
