<?xml version="1.0" encoding="UTF-8"?>

<xsl:stylesheet version="1.0"
xmlns:xsl="http://www.w3.org/1999/XSL/Transform">

<xsl:template match="/">

<html>

<head>
    <title>Football Players Information</title>
    <style>
        body {
            font-family: 'Segoe UI', Tahoma, Geneva, Verdana, sans-serif;
            background-color: #f8fafc;
            color: #1e293b;
            margin: 0;
            padding: 20px;
        }
        .container {
            max-width: 800px;
            margin: 0 auto;
        }
        h2 {
            text-align: center;
            color: #2563eb;
            margin-top: 30px;
        }
        table {
            width: 100%;
            border-collapse: collapse;
            margin-top: 20px;
            background: white;
            border-radius: 12px;
            overflow: hidden;
            box-shadow: 0 4px 6px rgba(0,0,0,0.05);
            border: 1px solid #e2e8f0;
        }
        th, td {
            padding: 15px;
            text-align: left;
            border-bottom: 1px solid #e2e8f0;
        }
        th {
            background-color: #f1f5f9;
            font-weight: 600;
            color: #475569;
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
            <a href="../Experiment_11/cricket.xml" class="btn">⬅ Back</a>
            <a href="../index.html" class="btn">🏠 Home</a>
            <a href="../Experiment_13/student.xml" class="btn">Continue ➡</a>
        </div>

        <h2>Football Players Information</h2>

<table border="1">

<tr bgcolor="lightblue">
<th>Name</th>
<th>Country</th>
<th>Position</th>
</tr>

<xsl:for-each select="footballplayers/player">

<tr>
<td><xsl:value-of select="name"/></td>
<td><xsl:value-of select="country"/></td>
<td><xsl:value-of select="position"/></td>
</tr>

</xsl:for-each>

</table>

    </div>
</body>

</html>

</xsl:template>

</xsl:stylesheet>
