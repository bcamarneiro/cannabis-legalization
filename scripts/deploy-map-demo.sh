#!/bin/bash
# Deploy script for Map Component demo
# Creates a static HTML page that loads the React component via CDN

set -e

mkdir -p public

# Copy the MapComponent.jsx to public
cp src/components/MapComponent.jsx public/

# Create the demo HTML page
cat > public/index.html << 'HTMLEOF'
<!DOCTYPE html>
<html lang="pt">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Mapa de Clubes Sociais - Cannabis Portugal</title>
    <style>
        * { margin: 0; padding: 0; box-sizing: border-box; }
        body { 
            font-family: -apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, sans-serif;
            background: #0f0f1a;
            color: #ffffff;
            min-height: 100vh;
        }
        .container {
            max-width: 1200px;
            margin: 0 auto;
            padding: 20px;
        }
        h1 {
            text-align: center;
            margin-bottom: 10px;
            color: #4dabf7;
        }
        .subtitle {
            text-align: center;
            color: #888;
            margin-bottom: 30px;
        }
    </style>
</head>
<body>
    <div class="container">
        <h1>Mapa de Clubes Sociais de Cannabis</h1>
        <p class="subtitle">Distribuição geográfica de 46 clubes em Portugal</p>
        <div id="root"></div>
    </div>
    
    <script src="https://unpkg.com/react@18/umd/react.development.js" crossorigin></script>
    <script src="https://unpkg.com/react-dom@18/umd/react-dom.development.js" crossorigin></script>
    <script src="https://unpkg.com/@babel/standalone/babel.min.js"></script>
    
    <script type="text/babel" src="MapComponent.jsx"></script>
    
    <script type="text/babel">
        const App = () => (
            <MapComponent />
        );
        const root = ReactDOM.createRoot(document.getElementById('root'));
        root.render(<App />);
    </script>
</body>
</html>
HTMLEOF

echo "Build complete - static demo page created in public/"
