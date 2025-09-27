import { 
  CognitoUser, 
  CognitoUserAttribute,
  AuthenticationDetails 
} from 'amazon-cognito-identity-js';
import { userPool } from './CognitoSetup';

export class AuthService {
  // Registro de usuario
  signUp = (email, password, attributes = {}) => {
    return new Promise((resolve, reject) => {
      const attributeList = [];
      
      // Agregar atributos personalizados
      Object.keys(attributes).forEach(key => {
        attributeList.push(new CognitoUserAttribute({
          Name: key,
          Value: attributes[key]
        }));
      });

      userPool.signUp(email, password, attributeList, null, (err, result) => {
        if (err) {
          reject(err);
          return;
        }
        resolve(result.user);
      });
    });
  };

  // Inicio de sesión
  signIn = (email, password) => {
    return new Promise((resolve, reject) => {
      const authenticationDetails = new AuthenticationDetails({
        Username: email,
        Password: password,
      });

      const cognitoUser = new CognitoUser({
        Username: email,
        Pool: userPool,
      });

      cognitoUser.authenticateUser(authenticationDetails, {
        onSuccess: (result) => {
          resolve({
            accessToken: result.getAccessToken().getJwtToken(),
            idToken: result.getIdToken().getJwtToken(),
            refreshToken: result.getRefreshToken().getToken(),
          });
        },
        onFailure: (err) => {
          reject(err);
        },
      });
    });
  };

  // Cerrar sesión
  signOut = () => {
    const cognitoUser = userPool.getCurrentUser();
    if (cognitoUser) {
      cognitoUser.signOut();
    }
  };

  // Obtener usuario actual
  getCurrentUser = () => {
    return new Promise((resolve, reject) => {
      const cognitoUser = userPool.getCurrentUser();

      if (!cognitoUser) {
        reject(new Error('No user found'));
        return;
      }

      cognitoUser.getSession((err, session) => {
        if (err) {
          reject(err);
          return;
        }

        cognitoUser.getUserAttributes((err, attributes) => {
          if (err) {
            reject(err);
            return;
          }

          const userData = {
            ...session,
            attributes: this.formatAttributes(attributes),
            username: cognitoUser.getUsername()
          };

          resolve(userData);
        });
      });
    });
  };

  formatAttributes = (attributes) => {
    const formatted = {};
    attributes.forEach(attribute => {
      formatted[attribute.Name] = attribute.Value;
    });
    return formatted;
  };
}

export const authService = new AuthService();