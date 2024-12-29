import { Camera, AlertCircle } from 'lucide-react';
import { Button } from '@/components/ui/button';
import { Card } from '@/components/ui/card';

interface CameraViewProps {
  selectedCamera: string;
  onSelectCamera: (camera: string) => void;
}

export function CameraView({ selectedCamera, onSelectCamera }: CameraViewProps) {
  return (
    <div className="grid gap-6">
      <div className="grid grid-cols-3 gap-4">
        {['Camera 1', 'Camera 2', 'Camera 3'].map((camera) => (
          <Button
            key={camera}
            variant={selectedCamera === camera ? "secondary" : "outline"}
            onClick={() => onSelectCamera(camera)}
            className="h-20"
          >
            <Camera className="mr-2 h-4 w-4" />
            {camera}
          </Button>
        ))}
      </div>

      <Card className="p-4 bg-muted/50 min-h-[300px] flex items-center justify-center">
        {selectedCamera ? (
          <div className="text-center text-muted-foreground">
            <Camera className="w-12 h-12 mx-auto mb-2" />
            <p>Viewing {selectedCamera}</p>
          </div>
        ) : (
          <div className="text-center text-muted-foreground">
            <AlertCircle className="w-12 h-12 mx-auto mb-2" />
            <p>Select a camera to view the feed</p>
          </div>
        )}
      </Card>
    </div>
  );
}