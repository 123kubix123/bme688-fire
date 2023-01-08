import { HttpClient, HttpErrorResponse } from '@angular/common/http';
import { Injectable } from '@angular/core';
import { Observable, throwError } from 'rxjs';
import { catchError } from 'rxjs/operators';
import { SensorData } from '../models/sensor_data.model';

@Injectable({
    providedIn: 'root',
})
export class SensorDataService {
    sensorDataUrl = 'https://sirserver.dynovski.xyz/sensor_data';

    constructor(private http: HttpClient) {}

    getSensorData(): Observable<SensorData> {
        return this.http.get<SensorData>(this.sensorDataUrl)
            .pipe(catchError(this.handleError));
    }

    private handleError(error: HttpErrorResponse): Observable<never> {
        if (error.status === 0) {
            // A client-side or network error occurred. Handle it accordingly.
            console.error('Wystąpił błąd: ', error);
        } else {
            // The backend returned an unsuccessful response code.
            // The response body may contain clues as to what went wrong.
            console.error(
                `Błąd serwera: ${error.status}, ` +
                    `szczegóły: ${error.statusText}`
            );
        }
        // Return an observable with a user-facing error message.
        return throwError('Wystąpił błąd aplikacji!');
    }
}