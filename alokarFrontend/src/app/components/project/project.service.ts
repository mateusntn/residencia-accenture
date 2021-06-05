import { HttpClient } from '@angular/common/http';
import { Injectable } from '@angular/core';
import { MatSnackBar } from '@angular/material/snack-bar';
import { Observable } from 'rxjs';
import { Project } from './project.model';

@Injectable({
    providedIn: 'root'
})
export class ProjectService {

    baseUrl = "http://localhost:3001/projects"

    constructor(private snackBar: MatSnackBar, private http: HttpClient) { }

    showMessage(msg: string) {
        this.snackBar.open(msg, 'x', {
            duration: 3000,
            horizontalPosition: "right",
            verticalPosition: "top"
        })
    }

    create(project: Project): Observable<Project> {
        return this.http.post<Project>(this.baseUrl, project)
    }

    read(): Observable<Project[]> {
        return this.http.get<Project[]>(this.baseUrl);
    }

    // readByPk(project: Project): Observable<Project> {
    //     return this.http.get<Project>(`${this.baseUrl}/${project.id}`)
    // }
}
