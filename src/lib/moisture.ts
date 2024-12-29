export const MOISTURE_THRESHOLDS = {
  LOW: 10,
  HIGH: 40
} as const;

export function calculateMoistureAverage(values: number[]): number {
  if (values.length === 0) return 0;
  return values.reduce((a, b) => a + b, 0) / values.length;
}