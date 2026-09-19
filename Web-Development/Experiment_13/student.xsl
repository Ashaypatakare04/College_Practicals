<?xml version="1.0"?>

<xsl:stylesheet version="1.0"
xmlns:xsl="http://www.w3.org/1999/XSL/Transform">

<xsl:template match="/">

<html>

<head>

<title>Student Application</title>

<style>

body{
    font-family: 'Segoe UI', Tahoma, Geneva, Verdana, sans-serif;
    background-color:#f8fafc;
    color: #1e293b;
    margin: 0;
    padding: 20px;
}

.container {
    max-width: 800px;
    margin: 0 auto;
}

table{
    width:100%;
    margin:auto;
    border-collapse:collapse;
    background:white;
    margin-top:30px;
    border-radius: 12px;
    overflow: hidden;
    box-shadow: 0 4px 6px rgba(0,0,0,0.05);
    border: 1px solid #e2e8f0;
}

th, td{
    border-bottom:1px solid #e2e8f0;
    padding:15px;
    text-align:center;
}

th{
    background-color:#f1f5f9;
    color:#475569;
    font-weight: 600;
}

h2{
    text-align:center;
    color:#2563eb;
    margin-top: 30px;
}

.button-container {
    margin-top: 32px;
    display: flex;
    justify-content: center;
    gap: 16px;
}
.btn {
    display: inline-block;
    padding: 10px 20px;
    background-color: #2563eb;
    color: white;
    text-decoration: none;
    border-radius: 6px;
    font-weight: 500;
    transition: 0.2s;
}
.btn:hover { background-color: #1e40af; }

</style>

</head>

<body>
    <div class="container">
        <div class="button-container">
            <a href="../Experiment_12/football.xml" class="btn">⬅ Back</a>
            <a href="../index.html" class="btn">🏠 Home</a>
        </div>

        <h2>Student Information</h2>

<table>

<tr>
<th>Name</th>
<th>Roll No</th>
<th>Branch</th>
<th>City</th>
</tr>

<xsl:for-each select="students/student">

<tr>
<td><xsl:value-of select="name"/></td>
<td><xsl:value-of select="rollno"/></td>
<td><xsl:value-of select="branch"/></td>
<td><xsl:value-of select="city"/></td>
</tr>

</xsl:for-each>

</table>

    </div>
</body>

</html>

</xsl:template>

</xsl:stylesheet>
