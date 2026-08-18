import React, { useRef, useEffect, useState, useCallback } from 'react';

/**
 * Map Component Shell - Cannabis Club Distribution
 * 
 * Displays interactive map of 46 cannabis social clubs across Portugal's districts.
 * Uses canvas ref for mounting and event listener hooks for interaction.
 * 
 * @param {Object} props
 * @param {Array} props.clubs - Array of club locations {id, name, district, lat, lng, members}
 * @param {Function} props.onClubSelect - Callback when a club is clicked
 * @param {String} props.initialZoom - Initial zoom level (default: 7)
 */
const MapComponent = ({ clubs = [], onClubSelect, initialZoom = 7 }) => {
  const canvasRef = useRef(null);
  const containerRef = useRef(null);
  const [selectedClub, setSelectedClub] = useState(null);
  const [isDragging, setIsDragging] = useState(false);
  const [zoom, setZoom] = useState(initialZoom);
  const [center, setCenter] = useState({ lat: 39.5, lng: -8.0 }); // Portugal center

  // Club data with district distribution (46 clubs total)
  const defaultClubs = [
    // Lisboa AML (9 clubs)
    { id: 1, name: 'Clube Lisboa Centro', district: 'Lisboa', lat: 38.7223, lng: -9.1393, members: 400 },
    { id: 2, name: 'Clube Lisboa Norte', district: 'Lisboa', lat: 38.7500, lng: -9.1500, members: 380 },
    { id: 3, name: 'Clube Lisboa Sul', district: 'Lisboa', lat: 38.7000, lng: -9.1300, members: 420 },
    { id: 4, name: 'Clube Lisboa Oriental', district: 'Lisboa', lat: 38.7300, lng: -9.1200, members: 390 },
    { id: 5, name: 'Clube Amadora', district: 'Amadora', lat: 38.7538, lng: -9.2308, members: 350 },
    { id: 6, name: 'Clube Oeiras', district: 'Oeiras', lat: 38.6979, lng: -9.3106, members: 360 },
    { id: 7, name: 'Clube Cascais', district: 'Cascais', lat: 38.6979, lng: -9.4215, members: 340 },
    { id: 8, name: 'Clube Sintra', district: 'Sintra', lat: 38.8029, lng: -9.3817, members: 370 },
    { id: 9, name: 'Clube Loures', district: 'Loures', lat: 38.8312, lng: -9.1667, members: 330 },
    // Porto AMP (8 clubs)
    { id: 10, name: 'Clube Porto Centro', district: 'Porto', lat: 41.1579, lng: -8.6291, members: 410 },
    { id: 11, name: 'Clube Porto Norte', district: 'Porto', lat: 41.1700, lng: -8.6200, members: 380 },
    { id: 12, name: 'Clube Porto Sul', district: 'Porto', lat: 41.1400, lng: -8.6300, members: 390 },
    { id: 13, name: 'Clube Vila Nova de Gaia', district: 'V.N. Gaia', lat: 41.1239, lng: -8.6118, members: 400 },
    { id: 14, name: 'Clube Gaia Sul', district: 'V.N. Gaia', lat: 41.1100, lng: -8.6200, members: 370 },
    { id: 15, name: 'Clube Matosinhos', district: 'Matosinhos', lat: 41.1821, lng: -8.6896, members: 350 },
    { id: 16, name: 'Clube Gondomar', district: 'Gondomar', lat: 41.1436, lng: -8.5378, members: 340 },
    { id: 17, name: 'Clube Maia', district: 'Maia', lat: 41.2344, lng: -8.6222, members: 360 },
    // Setúbal (4 clubs)
    { id: 18, name: 'Clube Setúbal', district: 'Setúbal', lat: 38.5244, lng: -8.8882, members: 380 },
    { id: 19, name: 'Clube Palmela', district: 'Palmela', lat: 38.5678, lng: -8.8978, members: 340 },
    { id: 20, name: 'Clube Barreiro', district: 'Barreiro', lat: 38.6631, lng: -9.0719, members: 350 },
    { id: 21, name: 'Clube Seixal', district: 'Seixal', lat: 38.6333, lng: -9.1000, members: 330 },
    // Braga (4 clubs)
    { id: 22, name: 'Clube Braga', district: 'Braga', lat: 41.5518, lng: -8.4229, members: 370 },
    { id: 23, name: 'Clube Braga Norte', district: 'Braga', lat: 41.5600, lng: -8.4300, members: 350 },
    { id: 24, name: 'Clube Guimarães', district: 'Braga', lat: 41.4452, lng: -8.2969, members: 360 },
    { id: 25, name: 'Clube Famalicão', district: 'Braga', lat: 41.4069, lng: -8.4558, members: 340 },
    // Aveiro (3 clubs)
    { id: 26, name: 'Clube Aveiro', district: 'Aveiro', lat: 40.6443, lng: -8.6455, members: 360 },
    { id: 27, name: 'Clube Águeda', district: 'Aveiro', lat: 40.5817, lng: -8.4436, members: 330 },
    { id: 28, name: 'Clube Ovar', district: 'Aveiro', lat: 40.8631, lng: -8.6419, members: 320 },
    // Coimbra (2 clubs)
    { id: 29, name: 'Clube Coimbra', district: 'Coimbra', lat: 40.2033, lng: -8.4103, members: 350 },
    { id: 30, name: 'Clube Figueira da Foz', district: 'Coimbra', lat: 40.1514, lng: -8.8614, members: 320 },
    // Faro/Algarve (2 clubs)
    { id: 31, name: 'Clube Faro', district: 'Faro', lat: 37.0194, lng: -7.9322, members: 340 },
    { id: 32, name: 'Clube Portimão', district: 'Faro', lat: 37.1390, lng: -8.5378, members: 330 },
    // Leiria (2 clubs)
    { id: 33, name: 'Clube Leiria', district: 'Leiria', lat: 39.7436, lng: -8.8071, members: 340 },
    { id: 34, name: 'Clube Marinha Grande', district: 'Leiria', lat: 39.7536, lng: -8.9319, members: 310 },
    // Viseu (2 clubs)
    { id: 35, name: 'Clube Viseu', district: 'Viseu', lat: 40.6566, lng: -7.9122, members: 330 },
    { id: 36, name: 'Clube Lamego', district: 'Viseu', lat: 41.0969, lng: -7.8069, members: 300 },
    // Santarém (2 clubs)
    { id: 37, name: 'Clube Santarém', district: 'Santarém', lat: 39.2369, lng: -8.6858, members: 330 },
    { id: 38, name: 'Clube Torres Novas', district: 'Santarém', lat: 39.4817, lng: -8.5369, members: 310 },
    // Viana do Castelo (1 club)
    { id: 39, name: 'Clube Viana do Castelo', district: 'Viana', lat: 41.6938, lng: -8.8336, members: 320 },
    // Vila Real (1 club)
    { id: 40, name: 'Clube Vila Real', district: 'Vila Real', lat: 41.3006, lng: -7.7444, members: 310 },
    // Évora (1 club)
    { id: 41, name: 'Clube Évora', district: 'Évora', lat: 38.5664, lng: -7.9069, members: 300 },
    // Beja (1 club)
    { id: 42, name: 'Clube Beja', district: 'Beja', lat: 38.0150, lng: -7.8650, members: 290 },
    // Castelo Branco (1 club)
    { id: 43, name: 'Clube Castelo Branco', district: 'Castelo Branco', lat: 39.8222, lng: -7.4908, members: 300 },
    // Bragança (1 club)
    { id: 44, name: 'Clube Bragança', district: 'Bragança', lat: 41.8069, lng: -6.7569, members: 290 },
    // Madeira (1 club)
    { id: 45, name: 'Clube Funchal', district: 'Madeira', lat: 32.6669, lng: -16.9241, members: 310 },
    // Açores (1 club)
    { id: 46, name: 'Clube Ponta Delgada', district: 'Açores', lat: 37.7394, lng: -25.6689, members: 300 },
  ];

  const clubData = clubs.length > 0 ? clubs : defaultClubs;

  // Convert lat/lng to canvas coordinates
  const latLngToCanvas = useCallback((lat, lng, canvasWidth, canvasHeight) => {
    const x = ((lng + 180) / 360) * canvasWidth;
    const latRad = (lat * Math.PI) / 180;
    const mercN = Math.log(Math.tan((Math.PI / 4) + (latRad / 2)));
    const y = (canvasHeight / 2) - (canvasWidth * mercN / (2 * Math.PI));
    return { x, y };
  }, []);

  // Draw the map
  const drawMap = useCallback(() => {
    const canvas = canvasRef.current;
    if (!canvas) return;

    const ctx = canvas.getContext('2d');
    const canvasWidth = canvas.width;
    const canvasHeight = canvas.height;

    // Clear canvas
    ctx.clearRect(0, 0, canvasWidth, canvasHeight);

    // Draw background
    ctx.fillStyle = '#1a1a2e';
    ctx.fillRect(0, 0, canvasWidth, canvasHeight);

    // Draw simplified Portugal outline (abstract representation)
    ctx.strokeStyle = '#4d4d6e';
    ctx.lineWidth = 2;
    ctx.beginPath();
    // Simplified Portugal border coordinates
    const portugalPath = [
      { x: canvasWidth * 0.35, y: canvasHeight * 0.25 },
      { x: canvasWidth * 0.45, y: canvasHeight * 0.28 },
      { x: canvasWidth * 0.48, y: canvasHeight * 0.35 },
      { x: canvasWidth * 0.45, y: canvasHeight * 0.45 },
      { x: canvasWidth * 0.42, y: canvasHeight * 0.55 },
      { x: canvasWidth * 0.38, y: canvasHeight * 0.65 },
      { x: canvasWidth * 0.35, y: canvasHeight * 0.70 },
      { x: canvasWidth * 0.32, y: canvasHeight * 0.65 },
      { x: canvasWidth * 0.30, y: canvasHeight * 0.55 },
      { x: canvasWidth * 0.28, y: canvasHeight * 0.45 },
      { x: canvasWidth * 0.30, y: canvasHeight * 0.35 },
    ];
    portugalPath.forEach((point, index) => {
      if (index === 0) ctx.moveTo(point.x, point.y);
      else ctx.lineTo(point.x, point.y);
    });
    ctx.closePath();
    ctx.stroke();

    // Draw clubs
    clubData.forEach((club) => {
      const pos = latLngToCanvas(club.lat, club.lng, canvasWidth, canvasHeight);
      
      // Adjust for zoom and center
      const adjustedX = (pos.x - canvasWidth / 2) * zoom + canvasWidth / 2;
      const adjustedY = (pos.y - canvasHeight / 2) * zoom + canvasHeight / 2;

      // Draw club marker
      ctx.beginPath();
      ctx.arc(adjustedX, adjustedY, selectedClub?.id === club.id ? 10 : 6, 0, Math.PI * 2);
      ctx.fillStyle = selectedClub?.id === club.id ? '#ff6b6b' : '#4dabf7';
      ctx.fill();
      ctx.strokeStyle = '#ffffff';
      ctx.lineWidth = 2;
      ctx.stroke();

      // Draw club label (only for selected or on hover)
      if (selectedClub?.id === club.id) {
        ctx.fillStyle = '#ffffff';
        ctx.font = '12px Arial';
        ctx.textAlign = 'center';
        ctx.fillText(club.name, adjustedX, adjustedY - 15);
        ctx.font = '10px Arial';
        ctx.fillText(`${club.members} membros`, adjustedX, adjustedY + 25);
      }
    });

    // Draw legend
    ctx.fillStyle = '#ffffff';
    ctx.font = '14px Arial';
    ctx.textAlign = 'left';
    ctx.fillText(`Total: ${clubData.length} clubes`, 20, 30);
    ctx.fillText(`Zoom: ${(zoom * 100).toFixed(0)}%`, 20, 50);
  }, [clubData, selectedClub, zoom, latLngToCanvas]);

  // Handle canvas click
  const handleCanvasClick = useCallback((e) => {
    if (isDragging) return;

    const canvas = canvasRef.current;
    const rect = canvas.getBoundingClientRect();
    const clickX = e.clientX - rect.left;
    const clickY = e.clientY - rect.top;

    // Check if click is near any club
    clubData.forEach((club) => {
      const pos = latLngToCanvas(club.lat, club.lng, canvas.width, canvas.height);
      const adjustedX = (pos.x - canvas.width / 2) * zoom + canvas.width / 2;
      const adjustedY = (pos.y - canvas.height / 2) * zoom + canvas.height / 2;
      
      const distance = Math.sqrt(Math.pow(clickX - adjustedX, 2) + Math.pow(clickY - adjustedY, 2));
      if (distance < 15) {
        setSelectedClub(club);
        if (onClubSelect) onClubSelect(club);
      }
    });
  }, [clubData, isDragging, latLngToCanvas, onClubSelect, zoom]);

  // Handle mouse down for dragging
  const handleMouseDown = useCallback((e) => {
    setIsDragging(true);
  }, []);

  // Handle mouse up
  const handleMouseUp = useCallback(() => {
    setIsDragging(false);
  }, []);

  // Handle wheel for zoom
  const handleWheel = useCallback((e) => {
    e.preventDefault();
    const delta = e.deltaY > 0 ? 0.9 : 1.1;
    setZoom((prev) => Math.min(Math.max(prev * delta, 3), 15));
  }, []);

  // Setup event listeners
  useEffect(() => {
    const canvas = canvasRef.current;
    if (!canvas) return;

    canvas.addEventListener('click', handleCanvasClick);
    canvas.addEventListener('mousedown', handleMouseDown);
    canvas.addEventListener('mouseup', handleMouseUp);
    canvas.addEventListener('mouseleave', handleMouseUp);
    canvas.addEventListener('wheel', handleWheel, { passive: false });

    return () => {
      canvas.removeEventListener('click', handleCanvasClick);
      canvas.removeEventListener('mousedown', handleMouseDown);
      canvas.removeEventListener('mouseup', handleMouseUp);
      canvas.removeEventListener('mouseleave', handleMouseUp);
      canvas.removeEventListener('wheel', handleWheel);
    };
  }, [handleCanvasClick, handleMouseDown, handleMouseUp, handleWheel]);

  // Redraw on state changes
  useEffect(() => {
    drawMap();
  }, [drawMap]);

  // Handle canvas resize
  useEffect(() => {
    const handleResize = () => {
      const canvas = canvasRef.current;
      const container = containerRef.current;
      if (!canvas || !container) return;

      const rect = container.getBoundingClientRect();
      canvas.width = rect.width;
      canvas.height = rect.height;
      drawMap();
    };

    handleResize();
    window.addEventListener('resize', handleResize);
    return () => window.removeEventListener('resize', handleResize);
  }, [drawMap]);

  return (
    <div
      ref={containerRef}
      style={{
        width: '100%',
        height: '600px',
        position: 'relative',
        backgroundColor: '#1a1a2e',
        borderRadius: '8px',
        overflow: 'hidden',
      }}
    >
      <canvas
        ref={canvasRef}
        style={{
          width: '100%',
          height: '100%',
          cursor: isDragging ? 'grabbing' : 'grab',
        }}
      />
      {selectedClub && (
        <div
          style={{
            position: 'absolute',
            bottom: '20px',
            left: '20px',
            backgroundColor: 'rgba(26, 26, 46, 0.9)',
            color: '#ffffff',
            padding: '15px',
            borderRadius: '8px',
            border: '1px solid #4dabf7',
            minWidth: '200px',
          }}
        >
          <h3 style={{ margin: '0 0 10px 0', fontSize: '16px' }}>{selectedClub.name}</h3>
          <p style={{ margin: '5px 0', fontSize: '12px' }}>Distrito: {selectedClub.district}</p>
          <p style={{ margin: '5px 0', fontSize: '12px' }}>Membros: {selectedClub.members}</p>
          <p style={{ margin: '5px 0', fontSize: '12px' }}>
            Coordenadas: {selectedClub.lat.toFixed(4)}, {selectedClub.lng.toFixed(4)}
          </p>
        </div>
      )}
    </div>
  );
};

export default MapComponent;
