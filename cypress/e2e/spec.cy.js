describe('Flujo E2E Taller', () => {
    it('Debe loguearse y crear tarea', () => {
      cy.visit('http://127.0.0.1:8000');
      
      cy.get('#username').type('admin');
      cy.get('#password').type('admin123');
      cy.get('#btn-login').click();
  
      cy.url().should('include', '/dashboard');
  
      cy.get('#task_name').type('Prueba con Cypress');
      cy.get('#priority').select('Media');
      cy.get('#btn-add').click();
  
      cy.get('#lista-tareas').should('contain', 'Prueba con Cypress');
    });
  });