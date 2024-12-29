import { Button } from '@/components/ui/button';
import { AlertCircle } from 'lucide-react';

interface WateringControlProps {
  isWatering: boolean;
  onToggle: () => void;
  autoMode?: boolean;
  autoAction: 'start' | 'stop' | null;
}

export function WateringControl({ 
  isWatering, 
  onToggle, 
  autoMode = false,
  autoAction 
}: WateringControlProps) {
  return (
    <div className="flex flex-col items-center gap-2">
      <Button
        onClick={onToggle}
        variant={isWatering ? "destructive" : "default"}
        className="min-w-[150px]"
      >
        {isWatering ? "Stop Watering" : "Start Watering"}
      </Button>
      
      {autoMode && autoAction && (
        <div className="flex items-center gap-2 text-sm text-muted-foreground">
          <AlertCircle className="w-4 h-4" />
          {autoAction === 'start' ? 'Low moisture detected!' : 'High moisture detected!'}
        </div>
      )}
    </div>
  );
}