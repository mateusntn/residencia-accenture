import { HttpClient } from '@angular/common/http';
import { Injectable } from '@angular/core';
import { MatSnackBar } from '@angular/material/snack-bar';
import { Observable } from 'rxjs';
import { Project } from './project.model';

@Injectable({
    providedIn: 'root'
})
export class ProjectService {

    

    constructor(private snackBar: MatSnackBar, private http: HttpClient) { }

    showMessage(msg: string) {
        this.snackBar.open(msg, 'x', {
            duration: 3000,
            horizontalPosition: "right",
            verticalPosition: "top"
        })
    }

    create(project: Project): Observable<Project> {
        const url = "http://localhost:5000/new_project";
        return this.http.post<Project>(url, project);
    }

    read(): Observable<Project[]> {
        const url = "http://localhost:5000/projects";
        return this.http.get<Project[]>(url);
    }

    update(newProject: Project, id: any): Observable<Project> {
        const url= `http://localhost:5000/projects/${id}`;
        return this.http.put<Project>(url, newProject);
    }

    readByPk(id: any): Observable<Project> {
        const url = "http://localhost:5000/projects";
        return this.http.get<Project>(`${url}/${id}`);
    }
}
