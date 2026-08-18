# Map Component - Cannabis Club Distribution

Interactive React component displaying the geographical distribution of 46 cannabis social clubs across Portugal's districts.

## Features

- **Canvas-based rendering** - High-performance map visualization using HTML5 canvas
- **Interactive controls** - Pan, zoom, and click interactions
- **Club selection** - Click on markers to view club details
- **Responsive design** - Adapts to container size
- **Customizable** - Accepts custom club data and callbacks

## Installation

```bash
# Ensure React 18+ is installed
npm install react react-dom
```

## Usage

### Basic Usage

```jsx
import MapComponent from './components/MapComponent';

function App() {
  return (
    <div>
      <h1>Mapa de Clubes Sociais</h1>
      <MapComponent />
    </div>
  );
}
```

### With Custom Club Data

```jsx
const customClubs = [
  { 
    id: 1, 
    name: 'Clube Lisboa', 
    district: 'Lisboa', 
    lat: 38.7223, 
    lng: -9.1393, 
    members: 400 
  },
  // ... more clubs
];

<MapComponent 
  clubs={customClubs} 
  initialZoom={8}
  onClubSelect={(club) => console.log('Selected:', club)}
/>
```

### With Event Handlers

```jsx
const handleClubSelect = (club) => {
  console.log(`Selected ${club.name} in ${club.district}`);
  // Navigate to club details page, show modal, etc.
};

<MapComponent 
  clubs={clubs} 
  onClubSelect={handleClubSelect}
/>
```

## Props

| Prop | Type | Default | Description |
|------|------|---------|-------------|
| `clubs` | `Array` | `[]` | Array of club objects. If empty, uses default 46 clubs distribution |
| `onClubSelect` | `Function` | `undefined` | Callback fired when a club marker is clicked |
| `initialZoom` | `Number` | `7` | Initial zoom level (3-15) |

### Club Object Structure

```typescript
interface Club {
  id: number;           // Unique identifier
  name: string;         // Club name
  district: string;     // District/region
  lat: number;          // Latitude coordinate
  lng: number;          // Longitude coordinate
  members: number;      // Number of active members
}
```

## Default Data

The component includes built-in data for 46 clubs distributed across Portugal:

- **Lisboa AML**: 9 clubs
- **Porto AMP**: 8 clubs
- **Setúbal**: 4 clubs
- **Braga**: 4 clubs
- **Aveiro**: 3 clubs
- **Coimbra**: 2 clubs
- **Faro (Algarve)**: 2 clubs
- **Leiria**: 2 clubs
- **Viseu**: 2 clubs
- **Santarém**: 2 clubs
- **Viana do Castelo**: 1 club
- **Vila Real**: 1 club
- **Évora**: 1 club
- **Beja**: 1 club
- **Castelo Branco**: 1 club
- **Bragança**: 1 club
- **Madeira**: 1 club
- **Açores**: 1 club

## Interactions

### Mouse Controls

- **Click** - Select a club marker to view details
- **Drag** - Pan the map (click and hold)
- **Wheel** - Zoom in/out (3x to 15x)

### Touch Controls

- **Tap** - Select a club marker
- **Swipe** - Pan the map
- **Pinch** - Zoom in/out

## Styling

The component uses inline styles for the container and canvas. To customize:

```jsx
<MapComponent />
// Container: backgroundColor: '#1a1a2e', borderRadius: '8px', height: '600px'
// Canvas: cursor: 'grab' / 'grabbing'
// Markers: '#4dabf7' (default), '#ff6b6b' (selected)
```

For theme customization, modify the `drawMap` function in `MapComponent.jsx`.

## Testing

Run tests with:

```bash
npm test -- MapComponent.test.jsx
```

### Test Coverage

- Component rendering
- Default club data (46 clubs)
- Custom club data
- Zoom interactions
- Club selection callbacks
- Event listener setup
- Responsive resize handling

## Performance Considerations

- Canvas rendering is optimized for 46 markers
- Event listeners are properly cleaned up on unmount
- `useCallback` prevents unnecessary re-renders
- Resize handler is debounced via requestAnimationFrame

## Browser Support

- Chrome 60+
- Firefox 55+
- Safari 12+
- Edge 79+

## Accessibility

- Canvas element includes ARIA role
- Selected club info is displayed in accessible panel
- Keyboard navigation support (future enhancement)

## Future Enhancements

- [ ] Keyboard navigation (arrow keys for pan, +/- for zoom)
- [ ] Club filtering by district
- [ ] Cluster markers for dense areas
- [ ] Export map as PNG/SVG
- [ ] Tooltip on hover
- [ ] District boundary overlays
- [ ] Real-time member count updates
- [ ] Integration with backend API

## License

CC BY-SA 4.0 - Same as parent repository

## References

- [React Documentation](https://react.dev/)
- [HTML5 Canvas API](https://developer.mozilla.org/en-US/docs/Web/API/Canvas_API)
- [Mermaid Diagrams](./README.md) - For static map alternatives
