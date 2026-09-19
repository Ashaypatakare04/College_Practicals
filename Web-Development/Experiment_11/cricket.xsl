<?xml version="1.0" encoding="UTF-8"?>
<xsl:stylesheet version="1.0" xmlns:xsl="http://www.w3.org/1999/XSL/Transform">

<xsl:template match="/">
<html>
<head>
    <title>Cricketers Information</title>
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
        }
        .player-card {
            background: white;
            margin-bottom: 20px;
            padding: 20px;
            border-radius: 12px;
            box-shadow: 0 4px 6px rgba(0,0,0,0.05);
            border: 1px solid #e2e8f0;
        }
        .name {
            font-size: 1.25rem;
            font-weight: 700;
            color: #1e40af;
            margin-bottom: 10px;
        }
        .info {
            font-size: 0.95rem;
            margin: 5px 0;
            color: #64748b;
        }
        .info b { color: #334155; }
        
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
        <h2>Cricketers Information</h2>
        
        <xsl:for-each select="cricketers/player">
            <div class="player-card">
                <div class="name"><xsl:value-of select="name"/></div>
                <div class="info"><b>Jersey No:</b> <xsl:value-of select="jersey"/></div>
                <div class="info"><b>Team:</b> <xsl:value-of select="team"/></div>
                <div class="info"><b>Role:</b> <xsl:value-of select="role"/></div>
            </div>
        </xsl:for-each>

        <div class="button-container">
            <a href="../Experiment_10/Resume.html" class="btn">⬅ Back</a>
            <a href="../index.html" class="btn">🏠 Home</a>
            <a href="../Experiment_12/football.xml" class="btn">Continue ➡</a>
        </div>
    </div>
</body>
</html>
</xsl:template>
</xsl:stylesheet>
