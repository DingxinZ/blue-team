  <main>
    <section class="registration">
      <h2>All messages</h2>
      <table>
        <tr>
          <td>From</td>
          <td>To</td>
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
