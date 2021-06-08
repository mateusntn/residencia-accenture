import { Component, OnInit } from '@angular/core';
import { Project } from '../project.model';
import { ProjectService } from '../project.service';
import { Router } from '@angular/router'

@Component({
    selector: 'app-project-create',
    templateUrl: './project-create.component.html',
    styleUrls: ['./project-create.component.css']
})
export class ProjectCreateComponent implements OnInit {

    project: Project = {
        nome: '',
        nomeEmpresa: '',
        descricao: '',
        custoPrevisto: 0,
        duracao: '',
        area: '',
        otherCost: 0,
        hardware: 0,
        licenca: 0,
        status: '',
        seatCharge: 0
    }

    constructor(private projectService: ProjectService, private router: Router) { }

    ngOnInit(): void {
    }


    createProject(): void {
        this.projectService.create(this.project).subscribe(() => {
            this.projectService.showMessage('Projeto criado com sucesso.');
            this.router.navigate([`/projects/`]);
        })
    }
}
